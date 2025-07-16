import time
from src.interfaces.interfaces import FinalPredictionInterface

OPERATOR_ADDRESS = "0xE45C3674E5672A391dC9367F0e94A3cE1049c177"
current_epoch = 1
commands = [
    {
        "name": "setOperator",
        "args": ["0x7DE4E5E811E9610027AC1b72538F0a26E1dBE816"],
        "value": 0,
    },
    {"name": "setMinBet", "args": [int(0.1 * 10**18)], "value": 0},
    {"name": "setMaxBet", "args": [int(10 * 10**18)], "value": 0},
    {"name": "startGenesis", "args": [], "value": 0},
]


def test_prediction_final(client):
    interface = FinalPredictionInterface
    for command in commands:
        try:
            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
                value=command["value"],
                estimate_gas=False,
            )

        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(2)
