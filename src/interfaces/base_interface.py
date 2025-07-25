import os
import json
from pathlib import Path
from loguru import logger
import traceback
from ..client.eth_client import EthClient
from .config import CONTRACT_CONFIG


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
                gas = 500000

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
