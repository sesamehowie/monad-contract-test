import time
from os import urandom
from src.interfaces.interfaces import NewChestsInterface

def test_new_chests(client):
    interface = NewChestsInterface

    try:
        interface.execute_write_function(
            function_name="withdraw",
            client=client,
            value=0,
            args=[int(500 * 10**18)],
            estimate_gas=False,
        )

    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(10)
