import time
from src.interfaces.interfaces import RockPaperScissorsInterface


def test_rps(client):
    interface = RockPaperScissorsInterface

    try:
        interface.execute_write_function(
            function_name="withdrawBankroll",
            client=client,
            args=[int(1200 * 10**18)],
        )
    except Exception as e:
        print(f"Error: {str(e)}")

        time.sleep(5)
