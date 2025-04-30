import time
from src.interfaces.interfaces import RouletteInterface

FUNCTIONS_TO_TEST = [
    {"name": "withdraw", "args": [int(300 * 10**18)]},
]


def test_roulette(client):
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
