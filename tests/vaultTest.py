import time
from src.interfaces.interfaces import VaultInterface
from src.interfaces.config import PREDICTION_FIX_CA

commands = [
    {"name": "authorizeGame", "value": 0, "args": [PREDICTION_FIX_CA]},
]


def test_vault(client):
    interface = VaultInterface
    for command in commands:
        try:

            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                value=command["value"],
                args=command["args"],
                estimate_gas=False,
            )

        except Exception as e:
            print(f"Error: {str(e)}")

        time.sleep(10)
