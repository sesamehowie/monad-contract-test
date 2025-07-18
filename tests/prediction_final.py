import time
from src.interfaces.interfaces import FinalPredictionInterface
import random


OPERATOR_ADDRESS = "0xE45C3674E5672A391dC9367F0e94A3cE1049c177"
current_epoch = 1


def test_prediction_final(client):
    interface = FinalPredictionInterface

    commands = [
        {
            "name": random.choice(["betPump", "betDump"]),
            "args": [],
            "value": int(0.15 * 10**18),
        }
        for _ in range(2)
    ]

    read_commands = [
        {"name": "currentRoundId", "args": []},
        {"name": "getUserClaimableAmount", "args": [client.address]},
        {"name": "getUserRounds", "args": [client.address]},
    ]

    # for command in commands:
    #     try:
    #         interface.execute_write_function(
    #             function_name=command["name"],
    #             client=client,
    #             args=command["args"],
    #             value=command["value"],
    #             estimate_gas=False,
    #         )
    #     except Exception as e:
    #         print(f"Error: {str(e)}")
    #     time.sleep(20)

    # time.sleep(20)

    for command in read_commands:
        try:
            interface.execute_read_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
            )
        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(2)
