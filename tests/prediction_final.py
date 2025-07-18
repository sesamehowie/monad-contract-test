import time
from src.interfaces.interfaces import FinalPredictionInterface


OPERATOR_ADDRESS = "0xE45C3674E5672A391dC9367F0e94A3cE1049c177"
current_epoch = 1


def test_prediction_final(client):
    interface = FinalPredictionInterface

    commands = [
        {
            "name": "cancelRound",
            "args": [
                6,
                [
                    "0x504e41550100000003b801000000040d02ec8cbd512b300a0240887f1ae3c00d74948d46e9da92fffc34f3befda59b94df2ce3054acbfbf173e83a1823d668ba87b48989efa9dc7b201abfd245f3fc0943010333d44a416508f710827802f618001fbbf2d9a7b8f9fb1fdb9ce9111519ab91ba4613d222b89d3d2d3588f2dc6f1c40216155686b105edf2f2dc7a54163c000940104aeb32e858b1e8e60d62598bd56300f053afdca5d676423bc92b8d5e68d2eda9e6b2e8f372577bee17befb4d73fed4f1a9b33d1f0e040fe913a5ebe458566148d0106bda45edccf2bf0c92b992100f5b0adac549fcd87938bc22b7a3ad2afcf3464044e758f3842c72f75756fc7afb37aececa44ab8fe28e217a504442188a078b307000a2f9b5099726a3e50af8a59ea355814c6564db51425d28bbdae708907ef0cc59810d6fd28f7493fa1e1613350db1d781976748897cb0268cd5f6f73598bf63bac000b1136e9a14402eb2a6d3689af38f3cb3b7a80486026bb44f756926667e79d0228320eb0e8f74a1623113645191e70b997526caced74a6e6022e376c08b8608755000c82391ad50f6cfc543e39b5d0151cc2cd3b45a3a8a7931961b7890fc047597eb65adb3debd03f80912bec3bf9d198f3aafdfc3210d9b3a6034efd1a1fa73a4680000d66844c2d350cf0dd19954e87946733108ef09086082e70a8610dec7b3156ab84431aed5f2bd95694bc82055085301458967fe8c35190b99873c532cdcc153745000ea925594e032f4df8e540a5c9c8d430583474c661bba24d67f1091603db48bf4c3ca5a435b039c74e7f45321240a3506142b4cad5f3d421a619c6d2087b0a4369000f1f68ef3a5e00df4972dbdb4378c0bb9cd5571e1c99a7e5f6f3e587fe08376e117ab9c96aee17f8c88cb37b60f8db0c75ecaea39dee6f6c63de0cdcdc3205ec0701103a3d0a3f37c77793d89cb5150d5d79200f44dda636dc19c43a8db624c93203dd5948faf12c3dda46ce0a006741e727146f46bcdf4ccd80cc7f38557f297441ec0111e0c4e4383ece2fbc68e1f2b3b5aba2634457d6f0cfb79f61ae49a5548b28944020534d5039caafa5c67d1fd6a7948046bf5661c6a4a943dd87b054772a5218be0112b308f6171f5711ebcc250e66c9502ff56a4dd9b0a8458a5bb2fd2269861a5bcf3a6d9a58c7fcd52c86648d51c00c58d5bab8da1ba148e9b32bdafdd30701ad4300687a261a00000000001ae101faedac5851e32b9b23b5f9411a8c2bac4aae3ed4dd7b811dd1a72ea4aa710000000008b014f3014155575600000000000dbda46400002710a98db5a422fce580b88291104d34aea7070fb64401005500e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b4300000ad3d17a65480000000178283bd5fffffff800000000687a261a00000000687a261900000ad107034f2000000000f89352940cfd26286da077b69b4df2fc52b574676f4900e2865891ba420a195e75d3d1a2c9f2b44cdb24fc81311c4f8bb494d2ec833c38de001eef315f7548109cb0fb20c8f29ff83eb9bbdfd2dce734e56abcbedbbeed84956e3398005af447547feaa43da1f8d40978c9a497a336531ab8464f451863fb514704ab9e6fa3187429a248e5e5400cae3c33e89e7e81d61aa8ca20f066d72313301f4f88510b1305a7cd6727e5a2ae6da84e5eb05031b436dce537ac29a42ec69d276c67a72cb8c48ecc59a0d715c33724e7e38987a3bc68dce28d29c4c0d23b856f1520bf82825b1a9e7e61fa83ba1aec231abfee010bd9f83fddd6"
                ],
            ],
            "value": 1,
        },
        # {
        #     "name": "betPump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "betDump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "betPump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "betDump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "betDump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "betPump",
        #     "args": [],
        #     "value": int(0.15 * 10**18),
        # },
        # {
        #     "name": "executeRound",
        #     "args": [
        #         [
        #             "0x504e41550100000003b801000000040d0289afbf187f6a573687d372131344bcbae075d7404df5abe810d14d246077b66c576422b0c470a6f1a7cea01c9086403f1c819246f5af9bd43f09df82cb79b1080003399b3569c05fac019dd4827aaca30b62fe185ceb20ddf3b2779d129498a9b55806b8a298a12c3bc7d1323a48c8a75279165f07c0b0be78b3d0321fce3bbe3e5c0004685368a6d37dc1be4e5498932549f9f3afc76cd2de50714f45fc3a77bee8fc290d56cf9292a0ffc13ca2d85bef913d804543e9fb70ec99d152e0f39e2fe88e12000664100a72c32eecfacd1f47ef3678961742579e711e45c8b49af33b3ecb3e85ca41a32acf01c0035a84a4f82ffd5f7ce17eadb9b3b7206e844165ac8f57ca2e6d00088ab2c8e542b52791ba02ed44d8e4f0ad457f782788e415c26bc8341fa6ef9eaa6ff6cce915c3cc43281d2b27169800a132fb47ecabd133ed7124abaee2383a57010a02371bad5ea8c0c9ee051a523ffc34e0d316778ee38afd4988e2e893548134841b89a0078ef3d6d6a190c1b668df0cdd64302de14684054f45f599499182c24e000b18e8fc9c3e4de86cb02dcce64f035f1e1ac362d2ff6765dce97f4ee1bef8283e1320bbff5af0cbea16fcc37e59194b93835cb6abc0c6ecba1491a6f2eba9367f010c27922ff47e2448be3fa4a5ed0fbf6530d4b43c5515ec6f299f8c1ef5247f0e5342b8bd1b68491c224e12e6e1244ed69d41989a11a0d5bd9f0ae26975b9b490c5010d59150cd9af523c4210ba546a97ca655f79fb8950494a2abffcb7faba61dea5120b9e45216eafb95877b60e06c6f424b9f4da8095ce0273c7da672ced09e206c8010e005b9927e812bfc29b769bc32610b5daab4a4157d30cd36839badee6e2b967ba590a916aba3de051120b552f98c0e565843da9a271d624f5fafbda96b5d21a15000f3932952bbc98a7feb4366644e4c427d376cdec871bc4dc11005a73f47914d0aa2c329593ad32f664b7ee062067e0703cfe1d512d4e3fa9b87f0af2d4ee6a9c5f0110f746a1abf56d1d29861be3a7c8ae36ac3bf4de6065002898a5cd9ad667116b5b77efaa5dc05ca650044b87a74d99b473b2247b1aeb441ea29b20fa1d825b08ca0011a0d38af360aa951aa3c03c59776cf90b4ab4f4ff7b9acbe7e131bd42f5238f8c533dfe4acc59b654beac3ae1c71fb65e663db53be233aac8c28bcbd62d70f19c016877a1c600000000001ae101faedac5851e32b9b23b5f9411a8c2bac4aae3ed4dd7b811dd1a72ea4aa710000000008a9f619014155575600000000000db7853b000027108298ab8e91b1dd795eb63e6abab97cea918de77501005500e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b4300000acbd2e147d7000000011ab5a46efffffff8000000006877a1c6000000006877a1c600000ad000a3a54000000000fed00be80c9b25c97e7173c0b4371126ebd8d7a5cd425dbe1620072560024102f9c4fc3b87fb8173d605bcfa031ea73ab6be5508573a49834f8ea3dad17b40e7116930d8c7cb64b19fad9e4e2924112fb94bd3389ffaa9d3c5a7eb6e133303ddf2deaaf2661412ee38b427085a17b56ba89c6d9a7ed75530fe08f8583847e64b1b8d8dc0d954d4ce8e5dd8014c8d16fd779fafe092f5cc0c2435d4634ed7c6e6835df2c400e46dd2ac16888498faf53dfdec444cb9265ebbf3c5f005875dc5e04b67058d54c3a1745689769041e74dea98d17d2e1a61bba9215c2183be14067e3fe07da1d243ed2cf3d6072362f15c01c6d3adc1db"
        #         ]
        #     ],
        #     "value": 1,
        # },
        # {
        #     "name": "betPump",
        #     "args": [],
        #     "value": int(1.5 * 10**18),
        # },
    ]

    read_commands = [
        {"name": "currentRoundId", "args": []},
        #     {"name": "getUserRounds", "args": [client.address]},
        #     {"name": "userBetsInRound", "args": [3]},
        # {"name": "getUserClaimableAmount", "args": [client.address]},
    ]

    for command in commands:
        try:
            interface.execute_write_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
                value=command["value"],
                estimate_gas=False,
            )
        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(10)

    for command in read_commands:
        try:
            interface.execute_read_function(
                function_name=command["name"],
                client=client,
                args=command["args"],
            )
        except Exception as e:
            print(f"Error: {str(e)}")
        time.sleep(2)
