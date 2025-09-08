from src.interfaces.interfaces import ChestsV3Interface

COMMANDS = [{"name": "withdraw", "value": 0, "args": [int(1900 * 10**18)]}]


def test_chests_v3(client):
    interface = ChestsV3Interface

    for command in COMMANDS:
        try:
            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
                value=command["value"],
                estimate_gas=False,
            )

        except Exception as e:
            print(f"Error: {str(e)}")
