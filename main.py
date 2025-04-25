from tests.rpsTest import test_rps
from tests.rouletteTest import test_roulette


def main():
    choice = int(input("1. Test RPS\n2. Test Roulette\n"))

    match choice:
        case 1:
            return test_rps()
        case 2:
            return test_roulette()
        case _:
            return


if __name__ == "__main__":
    main()
