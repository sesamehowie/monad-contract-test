import os
import sys
from tests.rpsTest import test_rps
from tests.rouletteTest import test_roulette
from tests.chestTest import test_chest
from tests.potTest import test_lottery, spam_test
from tests.plinkoTest import test_plinko
from tests.newRpsTest import test_new_rps
from tests.newChestTest import test_new_chests
from tests.chestsV3Test import test_chests_v3
from tests.predictionTest import test_prediction
from tests.vaultTest import test_vault
from tests.pythTest import test_pyth
from src.client.eth_client import EthClient
from dotenv import load_dotenv
from src.network.network import Monad

load_dotenv()


ADMIN_PKEY = os.environ.get("ADMIN_PKEY")
PLAYER1 = os.environ.get("PLAYER1")
PLAYER2 = os.environ.get("PLAYER2")
LOTTERY_PKEY = os.environ.get("LOTTERY_PKEY")
RPS_PLAYER = os.environ.get("RPS_PLAYER")


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
    rps_client = EthClient("rps player", RPS_PLAYER, Monad)

    while True:
        try:
            choice = int(
                input(
                    "1. Test RPS\n2. Test Roulette\n3. Test Chest\n4. Test Lottery\n5. MonRoll AutoTest\n6. Test Plinko\n7. Test new RPS\n8. Test new Chests\n9. Test Chests V3\n10. Test Prediction\n11. Test Vault\n12. Test Pyth\n"
                )
            )

            match choice:
                case 1:
                    test_rps(client)
                case 2:
                    test_roulette(client)
                case 3:
                    test_chest(client)
                case 4:
                    del client_items[2]
                    client_items.append(("admin", LOTTERY_PKEY))
                    test_lottery(get_clients(client_items))
                case 5:
                    player_clients = get_clients(player_client_items)
                    spam_test(player_clients, client)
                case 6:
                    test_plinko(client)
                case 7:
                    test_new_rps(client)
                case 8:
                    test_new_chests(client)
                case 9:
                    test_chests_v3(client)
                case 10:
                    test_prediction(client)
                case 11:
                    test_vault(client)
                case 12:
                    test_pyth(client)
                case _:
                    print("EXIT")
                    sys.exit(1)
        except Exception as e:
            print(f"Exception on entry point - {str(e)}")


if __name__ == "__main__":
    main()
