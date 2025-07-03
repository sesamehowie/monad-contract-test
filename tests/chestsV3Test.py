import time
from os import urandom
from src.interfaces.interfaces import ChestsV3Interface
from web3 import Web3

COMMANDS = [
    {
        "name": "openChests",
        "value": int(Web3.to_wei("0.627000001350000001", "ether")),
        "args": [
            [0, 0, 0],
            urandom(32),
        ],
    },
    {"name": "claimWinnings", "value": 0, "args": []},
    # {"name": "withdraw", "value": 0, "args": [int(1 * 10**18)]}
]


def test_chests_v3(client):
    interface = ChestsV3Interface

    # for command in COMMANDS:
    #     try:
    #         interface.execute_write_function(
    #             function_name=command["name"],
    #             client=client,
    #             args=command["args"],
    #             value=command["value"],
    #             estimate_gas=False,
    #         )

    #     except Exception as e:
    #         print(f"Error: {str(e)}")'

    # time.sleep(10)

    interface.execute_read_function(
        "playerWinnings", client, ["0xb66C8E76bF9B434bca77cd1B132A199D351C6bB5"]
    )
