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
                8,
                [
                    "0x504e41550100000003b801000000040d03f7199d9e6f69c27c9443b4bbe02d85b57df64a920bd090db1057d52267ef76f164640b3fc033fdbea7ea994bcb87d291334a6a5595834460e2831e09d63794fc0104cecfc1b3152d5c6fa57ec7428b520c86eb8f0d9525282c6d132bfd29511f4831233714b25714e4132787b52c621835a0c57c908378983d9a034a31b9ae28f15f00064e6274a2d768d9266c6308f263f4ebdaa5c31880f0c51a4cb6ec8df5bfbfd235002f83d1635114fdf4c6860a55c6af53a71d503b91e0d141cb065ee284e637e100087cfbdd214bb526d0b6e6a99f8efa615b566cbec075f085640e74f0b8ff8819e06cae2d2b3f097aa3eb63b3b48b58d8f93a890062e48920cf2f12796eff58c277000a5809e38ef1072f75e62b991053b730203463973b7c8b913420277c38ced3641f4d1c1892911ea5ab67cca23df2d5bf628c8e2edf7ebfe3d3e9499ef1d4f18e6b000b8b0684981845c576917a6fefc04ad143b9b64eb3864e52ed6ad40c548edca72c5a37c31e8c1c4d7fca63e2e49f343395fa3b5c9e6a9db97070a257686a7120f9010c8207475a7df7dc81d010f5b064e4927c167dbbf47ad084bdcb0e99a1d93ad7b73d6536f7ecd497101e8f903acae1cc7d76ff859ed7fccd700139d542511c1944010d55edd4a96665a80879dc0841a465521699590586735a32ac8e882c5e14f2ddd319b3fd3974e348b1282e8f36d19fda96cc249b86e4d174042aa2e5577308d7df000e13b322122c097b900559d8516273befa1ea234bf24df0fdef4e0ff317fed717c627ac5b9b0c5ab64c1089bd02306eceffc5e2149f53282b89fe72534742d4ca5000f4c9058418dc7253fd0c6b61447bb69b80a894a641da6dae6499607af45303f633adca3022c0eaa852af40f21b9ba9585bcc949cc05ee16c51b32c49ec22eb543011055835993425a791178cd4fe4145f223e0575ea9c3b772f975b6ca7a0e95d1c86204e51ec1cd2cefc3ca15e1ff627f53e207baca997f3bb11133c83fe028636dc0011c3ba3fc96572f09b9e2efc3186ff7a4383c8e33d097f3598384cf487c7944dff239eec30cf8550810a04bc90b745268aaa1f70b6219344741a2c3490d1e2aa630012ea4b4ff2afad3bd09b9a18eff22ce0d4be3e45a44fac5d2c7f50d9ee79618cbd781d5ba1e7e50aa51b0f9e9478b72261289b5f096a179d2632e465c7b5794f2401687a27ff00000000001ae101faedac5851e32b9b23b5f9411a8c2bac4aae3ed4dd7b811dd1a72ea4aa710000000008b01994014155575600000000000dbda90500002710ce4a23ee5e96aaa974ac2b5d087c52a8d614038801005500e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b4300000ad74337e1b200000000c976facefffffff800000000687a27ff00000000687a27ff00000ad1a7bb1ba000000000f96811dc0cfd26286da077b69b4df2fc52b574676f4900e28685375d503d674402f9459a8c45f9310aa066f5dc5c6fe74feb0a8d164cc171fbf38db5f9abb7e0dfbe79a8e56e7d802dc860533ed676b7beb917ac8a096b1ede82021272e6e4b15a0cf2ee436e557ad27964d4d15436c47ee1c02d99d8424d326f8592733744599271aecd00ea65f733151752e70cce117f2b8c05f21f9a33d1618e021ebe39b8e969004f087878d71b948a6092f584f3726c7a80539745775107bb47f77e9f33e0197fd1e04b4143f8ed03dafc23de0cb8eba851d0f9d18da2859dabc68405c5203c5cb7a4fe1a6dda0ccd72b2df6b934df9625871"
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
