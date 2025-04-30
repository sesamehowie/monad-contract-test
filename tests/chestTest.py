import time
from src.client.eth_client import EthClient
from config import ADMIN_PKEY
from src.network.network import Monad
from src.interfaces.interfaces import ChestsInterface

FUNCTIONS_TO_TEST = [
    {
        "name": "playerWinnings",
        "args": ["0x758E36a42De727c71370a55891b0Bf1bDF2c3f2D"],
    },
]


def test_chest():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    interface = ChestsInterface

    for item in FUNCTIONS_TO_TEST:
        fn_name = item["name"]
        arg = item["args"]

        try:
            interface.execute_read_function(
                function_name=fn_name,
                client=client,
                args=arg,
            )
        except Exception as e:
            print(f"Error on call {fn_name} with args {arg}: {str(e)}")

        time.sleep(5)
