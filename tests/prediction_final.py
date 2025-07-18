import time
from src.interfaces.interfaces import FinalPredictionInterface


OPERATOR_ADDRESS = "0xE45C3674E5672A391dC9367F0e94A3cE1049c177"
current_epoch = 1


def test_prediction_final(client):
    interface = FinalPredictionInterface

    commands = [
        # {
        #     "name": "cancelRound",
        #     "args": [
        #         10,
        #         [
        #             "0x504e41550100000003b801000000040d018c1fe0190aa690b6d8fdc30181b7c26e4bbb2c7d719d6e76186073d1feac423f03d1950ae767c26ec6fad8871b89a5e030b0c5d7b72d5b07174c48690bcb5d4c00035c653ac90c714cfd98cce42f43363b6e73575214b3f801eb78fa702e46f99afa34db0b37f35edade13a849b42e3e2277fae880410ad662689433828d748543e20004d4543603f15187f3bfd209498d35cc60bf78d9874f31421e40875129e9c7c8066730b8c4b941626b0e4e3f35a9ffc5aeccffae03d4f79960866013fbfd2187d00106361fae728e8f191c3593d5e06379fd177c96cfeb49c2fc31b26970e464da0d984253c00849a6ab183582bda95e7393080e8aab2e2dd70c4c2e097cdaee108553010845a54e6a3df792bf3a0cae959bcd4ef44abc4ceb8ecbe261c4dc6df5edd1efb713cc14519273ff1187db60353e9190a6957bdad31b057681040a2a0327a5c58a010a4a763e45018913f5296015a7d34138c84ae7131ca8325453f4b5d94ca48eea83259965a790e147f856379e301e29bfb343936022c0fc7cc38d8a9d3b2b1ae41e010bc8d1fc33b796e2d8c98581e52ee78de9ec0a61fb98d1735958f7890da9ff34ac78aa220bc2814cc001ff91708593aceac2db7411e524b2330f0a9a0a6f23b91b010ca16806deb2dc9f5331ed2886c7f2260913195e8a5d2f40275196df7392a40ef84fb8811e0b02ab68c4a6082605cb66d2af53347c019b513ab0a5af643e624508010d763c702cf79d5d8b69afa695a9d4311a83e27fa33e978f1489c8275ed48966ba3ac155cf7b54a9dc672ec0f415459797a0bd2a75bd8a619cd713270af7c42a53010ec4895ec9bcabfdea3ece5f58474652a332fadd470f7010f49f71167d29681e2159d5229842778d9ad6ea8791b1cfdc8a1623213b40cd7cff7bd5f753da3604690010e1df1632d1bc06096d23eadbaeb2d7ef3758607b8f0818c6b5f27b3f7b68820a585cd73ee3503c13ecf5a8f57113b225beb2e02352a56bdc6873081b8f86660d00118755e27077253a1720aaddc93df157b7c4be975f4d1bb67dedff50eaeb906da523ceb30fd83d9d052cc429958e0893d182759660bae00113dc43947298a9dbb201127afc21284effe2e3f6c184b17ba09688a1f3c867dfd4cca34e0b3dea0de7728073517f21feae86ebb95b465900e073a153993806d91f5e06863f88ddb31ba08a00687a395b00000000001ae101faedac5851e32b9b23b5f9411a8c2bac4aae3ed4dd7b811dd1a72ea4aa710000000008b043ce014155575600000000000dbdd33f00002710560986d57c0c9579ba52f328b0698a193907522501005500e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b4300000ada4c7017ea00000000da3ec99dfffffff800000000687a395b00000000687a395a00000ad4b2465be000000000e63f410c0cfd26286da077b69b4df2fc52b574676f4900e286a55a7fe52d78d1203da9f03f1d795ca2b8d3fa6a2f548132683f6a1a081806fcc574b3f0ad6566ad6f2c869ed196dfbdeb3aef74b543ad78dff986bfa189bf46977805be619c6d2e898f377d076dad2ef7e510b28f7b4577f3c8d3684dac4974134d6336bf2586a71e9b6d15cfc5ae12fb4aa4b8f86022507868befd5081ac145130290bc0d5da87972719f495faccac05c7502c7b7e633c8076c98bdc8b73c80a24c6f6cc8d9507075531ac2fd9c39bed6b250853ab891a3528b5663eef9765ea58733b600dfca0947543e73a57e5182c209dc49836c7968b1e3464"
        #         ],
        #     ],
        #     "value": 1,
        # },
        {
            "name": "betPump",
            "args": [],
            "value": int(0.15 * 10**18),
        },
        {
            "name": "betDump",
            "args": [],
            "value": int(0.15 * 10**18),
        },
        {
            "name": "betPump",
            "args": [],
            "value": int(0.15 * 10**18),
        },
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
