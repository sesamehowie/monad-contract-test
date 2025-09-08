from src.interfaces.interfaces import NewRpsInterface

COMMANDS = [
    {"name": "withdrawBankroll", "value": 0, "args": [int(500 * 10**18)]},
]


def test_new_rps(client):
    interface = NewRpsInterface

    for command in COMMANDS:
        try:
            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
                value=command["value"],
            )
        except Exception as e:
            print(f"Error: {str(e)}")
