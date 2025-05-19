import time
from src.interfaces.interfaces import PlinkoInterface


def test_plinko(client):
    interface = PlinkoInterface

    try:
        interface.execute_write_function(
            function_name="withdraw",
            client=client,
            args=[int(1350 * 10**18)],
        )
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(5)
