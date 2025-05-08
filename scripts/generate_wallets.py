import os
from eth_account import Account


def write_to_file(filename: str, data: list, mode: str):
    with open(filename, mode) as f:
        for line in data:
            f.write(line + "\n")

    return


def print_addrs(data: list):
    for pk in data:
        account = Account.from_key(pk)
        print(account.address)

    return


def generate_keys(amount: int) -> list:
    results = []

    for _ in range(amount):
        account = Account.create(extra_entropy=os.urandom(64))
        key = str(account.key.hex())
        results.append(key[2:] if key.startswith("0x") else key)

    return results


def main():
    amt = 30
    result_path = "scripts/results/generated_keys.txt"

    keys = generate_keys(amt)

    print_addrs(keys)
    write_to_file(result_path, keys, "w")


if __name__ == "__main__":
    main()
