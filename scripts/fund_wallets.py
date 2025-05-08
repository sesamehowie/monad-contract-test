import time
from web3 import Web3
from eth_account import Account

ADMIN_PKEY = ""
ADMIN_ACCOUNT = Account.from_key(ADMIN_PKEY)
ADMIN_ADDRESS = ADMIN_ACCOUNT.address

web3 = Web3(Web3.HTTPProvider("https://testnet-rpc.monad.xyz"))


def read_txt(filename: str):
    try:
        with open(filename, "r") as f:
            data = f.read().splitlines()
            return data
    except Exception as e:
        print(f"Error reading from file: {str(e)}")
        return []


def fund_wallet(receiver_addr: str, value: float):
    value_wei = int(value * 10**18)
    try:
        tx_data = {
            "from": ADMIN_ADDRESS,
            "to": Web3.to_checksum_address(receiver_addr),
            "nonce": web3.eth.get_transaction_count(ADMIN_ADDRESS),
            "chainId": web3.eth.chain_id,
            "gasPrice": int(Web3.to_wei(51, "gwei")),
            "gas": 25500,
            "value": value_wei,
        }
        signed = web3.eth.account.sign_transaction(tx_data, ADMIN_PKEY)
        tx_hash = web3.eth.send_raw_transaction(signed.raw_transaction)
        hex_hash = str(tx_hash.hex())
        normalized_hash = hex_hash if hex_hash.startswith("0x") else "0x" + hex_hash
        print(f"Transaction: https://testnet.monadexplorer.com/tx/{normalized_hash}")
        return True
    except Exception as e:
        print(f"Error sending tokens to {receiver_addr}: {str(e)}")
        return False


def main():
    amount_to_send = 0.05
    wallets = read_txt("scripts/results/generated_keys.txt")
    if not wallets:
        return

    addrs = [Account.from_key(key).address for key in wallets]

    for address in addrs:
        fund_wallet(address, amount_to_send)
        time.sleep(7)

    return True


if __name__ == "__main__":
    main()
