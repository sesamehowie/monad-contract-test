import os
import json
from pathlib import Path
from loguru import logger
from ..client.eth_client import EthClient


RPS_CA = "0x21730Db7aE00538A2ccfF5AFA602c37db1C0cC2f"
PLINKO_CA = "0xB320C0Db0e7D2FEEDa4CF09dbd009450561C551E"
ROULETTE_CA = "0x32aBcb3ec874c934Bfb81fC66bC7943bf3DAcDE7"
CHEST_CA = "0x801Bab7088890Ec76Db4841822D9ABc427A6AA8D"
LOTTERY_CA = "0x96DCb76f2bCa75f1d5592F5D6952abB8753F2885"


CONTRACT_CONFIG = {
    "RPS": RPS_CA,
    "Plinko": PLINKO_CA,
    "Roulette": ROULETTE_CA,
    "Chests": CHEST_CA,
    "Lottery": LOTTERY_CA,
}


class BaseInterface:
    def __init__(
        self,
        contract_name: str,
    ):
        self.contract_address = CONTRACT_CONFIG[contract_name]
        self.contract_name = contract_name
        self.abi = self.get_abi()

    def get_abi(self):
        cwd = Path(os.getcwd())
        abi_path = os.path.join(
            cwd, Path(f"src/contracts/{self.contract_name.lower()}/abi.json")
        )

        return json.load(open(abi_path))

    def execute_write_function(
        self, function_name: str, client: EthClient, args: list, value: int = 0
    ) -> bool:
        try:
            contract = client.get_contract(
                contract_addr=self.contract_address, abi=self.abi
            )

            logger.info(
                f"Contract {self.contract_name} | Executing write function {function_name} with args: {args}"
            )
            data = contract.encodeABI(fn_name=function_name, args=args)

            tx_params = {
                "from": client.address,
                "to": self.contract_address,
                "value": value,
                "nonce": client.get_nonce(),
                "chainId": client.network.chain_id,
                "gasPrice": client.w3.eth.gas_price,
                "gas": 500000,
                "data": data,
            }

            return client.sign_and_send_tx(tx_dict=tx_params)

        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return False

    def execute_read_function(self, function_name: str, client: EthClient, args: list):
        logger.info(
            f"Contract {self.contract_name} | Executing read function {function_name} with args: {args}"
        )

        contract = client.get_contract(
            contract_addr=self.contract_address, abi=self.abi
        )

        func = contract.get_function_by_name(function_name)

        if args is None:
            result = func().call()
        else:
            result = func(*args).call()

        logger.info(
            f"Call result of {function_name} on contract {self.contract_name}: {result}"
        )

        return result
