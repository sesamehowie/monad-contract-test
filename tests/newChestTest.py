import time
from os import urandom
from src.interfaces.interfaces import NewChestsInterface

COMMANDS = [
    {
        "name": "openChests",
        "value": int(),
        "args": [[0, 0, 0], urandom(32)],
    },
    {"name": "claimWinnings", "value": 0, "args": []},
    # {"name": "withdraw", "value": 0, "args": [int(1 * 10**18)]}
]


def test_new_chests(client):
    interface = NewChestsInterface

    for command in COMMANDS:
        try:
            # interface.execute_write_function(
            #     function_name=command["name"],
            #     client=client,
            #     value=command["value"],
            #     estimate_gas=False,
            # )
            interface.execute_read_function(
                function_name="requests", client=client, args=[2656070]
            )

        except Exception as e:
            print(f"Error: {str(e)}")

        time.sleep(10)
