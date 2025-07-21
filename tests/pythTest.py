import time
from src.interfaces.interfaces import PythInterface


commands = [
    {
        "name": "getPrice",
        "args": ["0xe62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43"],
    },
]


def test_pyth(client):
    interface = PythInterface
    for command in commands:
        try:

            interface.execute_read_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
            )

        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(2)
