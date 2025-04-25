import time
from src.client.eth_client import EthClient
from config import ADMIN_PKEY
from src.network.network import Monad
from src.interfaces.interfaces import RouletteInterface

FUNCTIONS_TO_TEST = [
    {"name": "withdraw", "args": [int(350 * 10**18)]},
]


def test_roulette():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    interface = RouletteInterface

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
