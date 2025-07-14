import time
from os import urandom
from src.interfaces.interfaces import PredictionInterface

OPERATOR_ADDRESS = "0xE45C3674E5672A391dC9367F0e94A3cE1049c177"
current_epoch = 1
commands = [
    {
        "name": "paused",
        "args": [],
    },
]


def test_prediction(client):
    interface = PredictionInterface
    for command in commands:
        try:

            interface.execute_read_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
            )

        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(2)
