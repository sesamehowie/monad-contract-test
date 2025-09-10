import os
import sys
from src.client.eth_client import EthClient
from dotenv import load_dotenv
from src.network.network import Monad
from tests import print_menu, ALL_TASKS, TASK_IDS

load_dotenv()


ADMIN_PKEY = os.environ.get("ADMIN_PKEY")
PLAYER1 = os.environ.get("PLAYER1")
PLAYER2 = os.environ.get("PLAYER2")
LOTTERY_PKEY = os.environ.get("LOTTERY_PKEY")
RPS_PLAYER = os.environ.get("RPS_PLAYER")
PRED_CLASSIC_OPERATOR = os.environ.get("PREDICTION_CLASSIC_OPERATOR_KEY")


def read_txt(filename):
    results = None
    try:
        with open(filename, "r") as f:
            results = f.read().splitlines()
        return results
    except Exception as e:
        print(f"Error opening {filename}: {str(e)}")
        return []


player_client_items = [
    (f"player {i}", player_key)
    for i, player_key in enumerate(
        read_txt(os.path.join(os.getcwd(), "scripts/results/generated_keys.txt"))
    )
]

client_items = [("player1", PLAYER1), ("player2", PLAYER2), ("admin", ADMIN_PKEY)]


def get_clients(keys):
    return [EthClient(name, key, Monad) for name, key in keys]


def main():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    operator_client = EthClient(
        account_name="classic operator",
        private_key=PRED_CLASSIC_OPERATOR,
        network=Monad,
    )

    while True:
        try:
            print_menu(ALL_TASKS)
            choice = int(input())
            if choice not in TASK_IDS:
                print("Choice not in task ids, exiting")
                sys.exit(1)
            else:
                task = ALL_TASKS[choice - 1]
                print("Selected task", task.name)

                if task.name == "MonRoll":
                    input_data = get_clients(client_items)
                elif task.name == "Prediction Game (Classic)":
                    input_data = operator_client
                else:
                    input_data = client

                task.task(input_data)

        except Exception as e:
            print(f"Exception on entry point - {str(e)}")


if __name__ == "__main__":
    main()
