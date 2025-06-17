import time
from src.interfaces.interfaces import ChestsInterface


def test_chest(client):
    interface = ChestsInterface

    try:
        interface.execute_write_function(
            function_name="withdraw",
            client=client,
            args=[int(800 * 10**18)],
        )
    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(5)
