import time
import random
from src.interfaces.interfaces import LotteryInterface


def test_lottery(clients):
    clientA, clientB, adminClient = clients

    """
    BETS
    """

    resA = LotteryInterface.execute_write_function("bet", clientA, [], int(5 * 10**16))
    assert resA
    time.sleep(2)
    resB = LotteryInterface.execute_write_function("bet", clientB, [], int(5 * 10**16))
    assert resB
    time.sleep(2)

    """
    ROUND CONTROLLER
    """

    LotteryInterface.execute_write_function(
        "setRoundController",
        adminClient,
        ["0xE45C3674E5672A391dC9367F0e94A3cE1049c177"],
    )

    """
    ROUND STATE
    """

    resRoundState = LotteryInterface.execute_read_function(
        "roundState", adminClient, []
    )
    assert isinstance(resRoundState, int)
    resReadyToLock = LotteryInterface.execute_read_function(
        "readyToLock", adminClient, []
    )
    assert resReadyToLock is not None
    time.sleep(5)

    """
    LATE BET TEST
    """

    time.sleep(90)
    randClient = random.choice([clientA, clientB])

    resC = LotteryInterface.execute_write_function(
        "bet", randClient, [], int(5 * 10**16)
    )
    assert resC

    """
    SPAM TEST
    """

    counter = 0
    while True:
        try:
            res = LotteryInterface.execute_write_function(
                "bet", clientA, [], int(5 * 10**16)
            )
            if not res:
                counter += 1
        except Exception as e:
            print(f"Error: {str(e)}")
            if "insufficient balance" in str(e):
                break
        finally:
            if counter >= 15:
                break
            time.sleep(1)
    time.sleep(5)

    """
    GAME ID RETRIEVAL
    """

    # transaction_receipt = adminClient.w3.eth.get_transaction_receipt(
    #     "0x4b1e216ae13bba3758979182d74caeeebf8d8754cdee716fce6adb0688030f8e"
    # )

    # game_id = int.from_bytes(transaction_receipt["logs"][0]["data"], byteorder="big")

    """
    WAIT AND LOCK ROUND
    """

    time.sleep(65)
    resLock = LotteryInterface.execute_write_function(
        "lockRound", adminClient, [], True
    )
    assert resLock

    """
    WAIT AND SETTLE ROUND
    """

    time.sleep(20)
    resSettle = LotteryInterface.execute_write_function(
        "settleRound", adminClient, [], 0, True
    )
    assert resSettle

    """
    CANCEL ROUND
    """

    resCancel = LotteryInterface.execute_write_function("cancelRound", adminClient, [])
    assert resCancel
    time.sleep(5)

    """
    CLAIM
    """

    for client in [clientA, clientB]:
        resRefund = LotteryInterface.execute_write_function(
            "claim", client, [client.address]
        )
        assert resRefund
        time.sleep(5)

    """
    EMERGENCY RECOVER
    """

    resEmergencyRecover = LotteryInterface.execute_write_function(
        "emergencyRecoverFunds", adminClient, [adminClient.address]
    )
    assert resEmergencyRecover
    time.sleep(5)

    """
    UNPAUSE
    """

    resUnpause = LotteryInterface.execute_write_function("unpause", adminClient, [])
    assert resUnpause
    time.sleep(5)

    """
    CHECK WINNINGS
    """

    resWinningsCheck = [
        LotteryInterface.execute_read_function(
            "credit", clientItem, [clientItem.address]
        )
        for clientItem in [clientA, clientB]
    ]
    assert all(item == 0 for item in resWinningsCheck)

    """
    CLAIM REFUND
    """

    resRefund = [
        LotteryInterface.execute_write_function(
            "claimRefund", clientItem, [clientItem.address]
        )
        for clientItem in [clientA, clientB]
    ]
    assert resRefund


def spam_test(clients, admin_client):
    check_interval = 10
    sleep_between_rounds = 90
    curr_divider = 0
    seconds_elapsed = 0
    round_state = 0
    round_count = 1
    winners_list = []

    while True:
        try:
            print(f"Round {round_count} | Starting")

            random_clients = [random.choice(clients) for _ in range(4, 30)]
            print(f"Player Count: {len(random_clients)}")

            for client in random_clients:
                if len(winners_list) > 0:
                    if client.address.lower() in [
                        item.lower() for item in winners_list
                    ]:
                        LotteryInterface.execute_write_function(
                            "claim", client, [client.address]
                        )
                        for winner in winners_list:
                            if winner.lower() == client.address.lower():
                                winners_list.remove(winner)
                                break

                LotteryInterface.execute_write_function(
                    "bet", client, [], int(round(random.uniform(0.05, 0.1), 4) * 10**18)
                )
                time.sleep(5)
                seconds_elapsed += 5

                if round_state == 3:
                    for _ in range(3):
                        print(f"Round {round_count} LOCKED, waiting for results")
                        time.sleep(sleep_between_rounds / 3)
                        round_state = LotteryInterface.execute_read_function(
                            "roundState", admin_client, []
                        )

                        if round_state == 4:
                            round_info = LotteryInterface.execute_read_function(
                                "cur", admin_client, []
                            )
                            winner_address = round_info[len(round_info) - 1]
                            if winner_address is not None:
                                if winner_address not in winners_list:
                                    winners_list.append(winner_address)
                                    break
                        if round_state == 0 or round_state == 1:
                            prev_info = LotteryInterface.execute_read_function(
                                "prev", admin_client, []
                            )
                            winner_address = prev_info[len(prev_info) - 3]
                            if winner_address is not None:
                                if winner_address not in winners_list:
                                    winners_list.append(winner_address)
                                    break

                    curr_divider = 0
                    seconds_elapsed = 0
                    round_state = 0
                    round_count += 1
                    break

                if seconds_elapsed // check_interval > curr_divider:
                    round_state = LotteryInterface.execute_read_function(
                        "roundState", admin_client, []
                    )
                    print("Current Phase:", round_state)
                    print("Round type: ", type(round_state))
                    curr_divider += 1

        except Exception as e:
            print(f"Caught exception during round {round_count}: {str(e)}")
            curr_divider = 0
            seconds_elapsed = 0
            round_state = 0
            round_count += 1
        finally:
            time.sleep(sleep_between_rounds)
