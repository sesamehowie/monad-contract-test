from src.interfaces.interfaces import PredictionClassicInterface


def test_prediction_classic(client):
    interface = PredictionClassicInterface

    try:
        # interface.execute_write_function(
        #     function_name="betPump", client=client, args=[], value=int(10**18)
        # )
        # time.sleep(5)
        # interface.execute_write_function(
        #     function_name="betDump", client=client, args=[], value=int(2 * 10**18)
        # )
        interface.execute_write_function("claimAllRewards", client, [], value=0)

    except Exception as e:
        print(f"Error: {str(e)}")
