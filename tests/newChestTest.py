import time
from os import urandom
from src.interfaces.interfaces import NewChestsInterface

def test_new_chests(client):
    interface = NewChestsInterface

    try:
        # interface.execute_write_function(
        #     function_name=command["name"],
        #     client=client,
        #     value=command["value"],
        #     estimate_gas=False,
        # )
        interface.execute_read_function(
            "playerWinnings", client, ["0xb66C8E76bF9B434bca77cd1B132A199D351C6bB5"]
        )

    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(10)
