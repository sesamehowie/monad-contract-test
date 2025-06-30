import time
from src.interfaces.interfaces import RockPaperScissorsInterface


def test_rps(client):
    interface = RockPaperScissorsInterface

    interface.execute_read_function("totalPendingWinnings", client, [])

    try:
        interface.execute_write_function(
            function_name="withdrawBankroll",
            client=client,
            args=[int(500 * 10**18)],
        )
    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(5)
