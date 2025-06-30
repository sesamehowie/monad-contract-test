import time
# from os import urandom
from loguru import logger
from src.interfaces.interfaces import NewRpsInterface

COMMANDS = [
    # {"name": "setMinBet", "value": 0, "args": [int(0.1 * 10**18)]},
    # {"name": "setMaxBet", "value": 0, "args": [int(50 * 10**18)]},
    # {"name": "claimWinnings", "value": 0, "args": []},
    # {"name": "play", "value": int(0.127 * 10**18), "args": [0, urandom(32)]},
    # {"name": "claimWinnings", "value": 0, "args": []},
    # {"name": "play", "value": int(0.127 * 10**18), "args": [1, urandom(32)]},
    # {"name": "claimWinnings", "value": 0, "args": []},
    # {"name": "play", "value": int(0.127 * 10**18), "args": [2, urandom(32)]},
    # {"name": "claimWinnings", "value": 0, "args": []},
    {"name": "withdrawBankroll", "value": 0, "args": [int(500 * 10**18)]},
]


def fund_contract(admin_client, amount: float | int):
    contract_addr = NewRpsInterface.contract_address
    amt = admin_client.w3.to_wei(amount, "ether")
    tx = {
        "from": admin_client.address,
        "to": contract_addr,
        "nonce": admin_client.get_nonce(),
        "chainId": admin_client.network.chain_id,
        "gasPrice": int(51 * 10**9),
        "gas": 50000,
        "value": amt,
    }
    return admin_client.sign_and_send_tx(tx)


def test_new_rps(client):
    interface = NewRpsInterface

    logger.info("MinBet:")
    interface.execute_read_function("minBet", client, [])
    logger.info("MaxBet:")
    interface.execute_read_function("maxBet", client, [])

    for command in COMMANDS:
        try:
            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
                value=command["value"],
            )
        except Exception as e:
            print(f"Error: {str(e)}")

        time.sleep(5)
