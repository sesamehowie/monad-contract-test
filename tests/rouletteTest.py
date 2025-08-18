from src.interfaces.interfaces import RouletteInterface


def test_roulette(client):
    interface = RouletteInterface

    try:
        interface.execute_write_function(
            function_name="withdraw",
            client=client,
            args=[int(2700 * 10**18)],
        )
    except Exception as e:
        print(f"Error: {str(e)}")
