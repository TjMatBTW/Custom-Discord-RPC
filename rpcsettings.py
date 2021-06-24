import rpc
import time

client_id = '[PUT YOUR CLIENT ID HERE]' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Sample State",
            "details": "Sample Details",
            "assets": {
                "large_text": "Sample Text",
                "large_image": "[image name]", #Read the ``README.mb`` to understand this.
                "small_text": "Sample Text but smaller",
                "small_image":"[image name but smaller lol]" #Read the ``README.mb`` to understand this.
            },
            "buttons": [
                {
                    "label":"[Any button display name you want]",
                    "url": "[Any Link you want]"
                },
                {
                    "label":"[Any button display name you want]",
                    "url": "[Any Link you want]"
                }
            ]
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)
