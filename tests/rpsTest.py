import time
from src.client.eth_client import EthClient
from config import ADMIN_PKEY
from src.network.network import Monad
from src.interfaces.interfaces import RockPaperScissorsInterface


FUNCTIONS_TO_TEST = [
    {"name": "play", "args": [0]},
    {"name": "play", "args": [4]},
    {"name": "claimWinnings", "args": []},
    {"name": "setMinBet", "args": [int(0.1 * 10**18)]},
    {"name": "setMaxBet", "args": [int(100 * 10**18)]},
    {"name": "withdrawBankroll", "args": [int(1 * 10**18)]},
]


def test():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    interface = RockPaperScissorsInterface

    for item in FUNCTIONS_TO_TEST:
        fn_name = item["name"]
        arg = item["args"]

        try:
            interface.execute_write_function(
                function_name=fn_name,
                client=client,
                args=arg,
                value=int(0.1 * 10**18) if fn_name == "play" else 0,
            )
        except Exception as e:
            print(f"Error on call {fn_name} with args {arg}: {str(e)}")

        time.sleep(5)
