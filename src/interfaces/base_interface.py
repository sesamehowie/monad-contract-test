import os
import json
from pathlib import Path
from loguru import logger
import traceback
from ..client.eth_client import EthClient


RPS_CA = "0x21730Db7aE00538A2ccfF5AFA602c37db1C0cC2f"
PLINKO_CA = "0xB320C0Db0e7D2FEEDa4CF09dbd009450561C551E"
ROULETTE_CA = "0x32aBcb3ec874c934Bfb81fC66bC7943bf3DAcDE7"
CHEST_CA = "0x801Bab7088890Ec76Db4841822D9ABc427A6AA8D"
LOTTERY_CA = "0x992596F29e89E376E0B8DA5b3bcF12727A4CB736"
NEW_RPS_CA = "0x77371f7452AFF5FcaA3A3B59A11794dB19Af5981"
NEW_CHESTS_CA = "0x101711403B2E45B0a53512E43e3232C4d5A78cA5"
CHESTS_V3_CA = "0x80f9cefc95699b7941dFA1F52c9c75d7C5e361Bd"
VAULT_CA = "0x01e4Fe20Fd7e65865B0aF3b0eDccEF135c3E1F5A"
PREDICTION_CA = "0x0f68d96d5f684121dB47634B1B21626Fa1733556"


CONTRACT_CONFIG = {
    "RPS": RPS_CA,
    "Plinko": PLINKO_CA,
    "Roulette": ROULETTE_CA,
    "Chests": CHEST_CA,
    "Lottery": LOTTERY_CA,
    "New_RPS": NEW_RPS_CA,
    "New_Chests": NEW_CHESTS_CA,
    "ChestsV3": CHESTS_V3_CA,
    "Vault": VAULT_CA,
    "Prediction": PREDICTION_CA,
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
        self,
        function_name: str,
        client: EthClient,
        args: list,
        value: int = 0,
        estimate_gas: bool = False,
        build_transaction: bool = False,
    ) -> bool:
        try:
            contract = client.get_contract(
                contract_addr=self.contract_address, abi=self.abi
            )

            logger.info(
                f"Contract {self.contract_name} | Executing write function {function_name} with args: {args}"
            )
            if build_transaction:
                func = contract.get_function_by_name(function_name)
                if args:
                    tx_params = func(*args).build_transaction(
                        {
                            "from": client.address,
                            "nonce": client.get_nonce(),
                            "chainId": client.network.chain_id,
                            "gasPrice": int(client.w3.to_wei(51, "gwei")),
                        }
                    )
                else:
                    tx_params = func().build_transaction(
                        {
                            "from": client.address,
                            "nonce": client.get_nonce(),
                            "chainId": client.network.chain_id,
                            "gasPrice": int(client.w3.to_wei(51, "gwei")),
                        }
                    )
            else:
                data = contract.encodeABI(fn_name=function_name, args=args)

                tx_params = {
                    "from": client.address,
                    "to": self.contract_address,
                    "value": value,
                    "nonce": client.get_nonce(),
                    "chainId": client.network.chain_id,
                    "gasPrice": int(client.w3.to_wei(51, "gwei")),
                    "data": data,
                }

            if estimate_gas:
                gas = client.w3.eth.estimate_gas(tx_params)
            else:
                gas = 300000

            tx_params["gas"] = gas

            return client.sign_and_send_tx(tx_dict=tx_params)

        except Exception:
            logger.error(f"Error: {traceback.format_exc()}")
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
