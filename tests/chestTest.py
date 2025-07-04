import time
from src.interfaces.interfaces import ChestsInterface


def test_chest(client):
    interface = ChestsInterface

    try:
        interface.execute_read_function(
            "playerWinnings", client, ["0xb66C8E76bF9B434bca77cd1B132A199D351C6bB5"]
        )
        # interface.execute_write_function(
        #     function_name="withdraw",
        #     client=client,
        #     args=[int(3000 * 10**18)],
        # )
    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(5)
