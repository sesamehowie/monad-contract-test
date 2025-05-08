import time
from src.interfaces.interfaces import LotteryInterface

def test_lottery(clients):
    clientA, clientB, adminClient = clients

    # LotteryInterface.execute_write_function(
    #     "setRoundController",
    #     adminClient,
    #     ["0xE45C3674E5672A391dC9367F0e94A3cE1049c177"],
    # )

    # time.sleep(5)

    for client in clients:
        print(f"Client {client.account_name} address: {client.address}")

    # resA = LotteryInterface.execute_write_function("bet", clientA, [], int(1 * 10**17))
    # assert resA
    # time.sleep(5)
    # resB = LotteryInterface.execute_write_function("bet", clientB, [], int(1 * 10**17))
    # assert resB
    # time.sleep(5)

    # transaction_receipt = adminClient.w3.eth.get_transaction_receipt(
    #     "0x4b1e216ae13bba3758979182d74caeeebf8d8754cdee716fce6adb0688030f8e"
    # )

    # game_id = int.from_bytes(transaction_receipt["logs"][0]["data"], byteorder="big")
    # time.sleep(65)
    resLock = LotteryInterface.execute_write_function("lockRound", adminClient, [])
    assert resLock
    time.sleep(15)
    resSettle = LotteryInterface.execute_write_function("settleRound", adminClient, [])
    assert resSettle
    # resEmergencyRecover = LotteryInterface.execute_write_function(
    #     "emergencyRecoverFunds", adminClient, [adminClient.address]
    # )
    # assert resEmergencyRecover
    # time.sleep(5)
    # resUnpause = LotteryInterface.execute_write_function("unpause", adminClient, [])
    # assert resUnpause
    # time.sleep(5)

    # resWinningsCheck = [
    #     LotteryInterface.execute_read_function(
    #         "credit", clientItem, [clientItem.address]
    #     )
    #     for clientItem in [clientA, clientB]
    # ]
    # assert all(item == 0 for item in resWinningsCheck)

    # resClaims = [
    #     LotteryInterface.execute_write_function(
    #         "claim", clientItem, [clientItem.address]
    #     )
    #     for clientItem in [clientA, clientB]
    # ]
    # assert resClaims
    # resUnpause = LotteryInterface.execute_write_function("unpause", adminClient, [])
    # assert resUnpause
