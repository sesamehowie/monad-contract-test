import os
from tests.rpsTest import test_rps
from tests.rouletteTest import test_roulette
from tests.chestTest import test_chest
from tests.potTest import test_lottery
from src.client.eth_client import EthClient
from dotenv import load_dotenv
from src.network.network import Monad

load_dotenv()

ADMIN_PKEY = os.environ.get("ADMIN_PKEY")
PLAYER1 = os.environ.get("PLAYER1")
PLAYER2 = os.environ.get("PLAYER2")

client_items = [("player1", PLAYER1), ("player2", PLAYER2), ("admin", ADMIN_PKEY)]


def get_clients(keys):
    return [EthClient(name, key, Monad) for name, key in keys]


def main():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    choice = int(
        input("1. Test RPS\n2. Test Roulette\n3. Test Chest\n4. Test Lottery\n")
    )

    match choice:
        case 1:
            return test_rps(client)
        case 2:
            return test_roulette(client)
        case 3:
            return test_chest(client)
        case 4:
            return test_lottery(get_clients(client_items))
        case _:
            return


if __name__ == "__main__":
    main()
