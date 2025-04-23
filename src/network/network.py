class Network:
    def __init__(
        self,
        name: str,
        chain_id: int,
        native_token: str,
        rpc_list: list[str],
        scanner: str,
    ):
        self.name = name
        self.chain_id = chain_id
        self.token = native_token
        self.rpc_list = rpc_list
        self.scanner = scanner


Monad = Network(
    "Monad Testnet",
    10143,
    "MON",
    ["https://testnet-rpc.monad.xyz"],
    "https://testnet.monadexplorer.com",
)
