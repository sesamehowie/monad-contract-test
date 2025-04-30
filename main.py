from tests.rpsTest import test_rps
from tests.rouletteTest import test_roulette
from tests.chestTest import test_chest
from src.client.eth_client import EthClient
from config import ADMIN_PKEY
from src.network.network import Monad


def main():
    client = EthClient(
        account_name="admin wallet", private_key=ADMIN_PKEY, network=Monad
    )
    choice = int(input("1. Test RPS\n2. Test Roulette\n3. Test Chest\n"))

    match choice:
        case 1:
            return test_rps(client)
        case 2:
            return test_roulette(client)
        case 3:
            return test_chest(client)
        case _:
            return


if __name__ == "__main__":
    main()
