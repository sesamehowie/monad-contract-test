import time
from src.interfaces.interfaces import ChestsInterface

FUNCTIONS_TO_TEST = [
    {
        "name": "withdraw",
        "args": [int(15 * 10**20)],
    },
]


def test_chest(client):
    interface = ChestsInterface

    for item in FUNCTIONS_TO_TEST:
        fn_name = item["name"]
        arg = item["args"]

        try:
            interface.execute_write_function(
                function_name=fn_name,
                client=client,
                args=arg,
            )
        except Exception as e:
            print(f"Error on call {fn_name} with args {arg}: {str(e)}")

        time.sleep(5)
