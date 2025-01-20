import json
import requests
from instaloader import Instaloader, Profile
ZAPIER_WEBHOOK_URL = "https://hook.eu2.make.com/xav55tvf7eri6hw1t6j41xx5qtm24j53"

def upload_to_make(file_path,type, caption=""):
    response = requests.post(
        ZAPIER_WEBHOOK_URL,
        data={"caption": caption,
                "file": {file_path},
                "type": type
                }
    )
    if response.status_code == 200:
        print("Successfully uploaded to Zapier.")
    else:
        print("Failed to upload:", response.text)

def upload_to_make_multiple(file_paths,type, caption=""):
    file_paths_json  = json.dumps(file_paths)
    response = requests.post(
        ZAPIER_WEBHOOK_URL,
        data={"caption": caption,
                "file": file_paths_json,
                "type": type
                }
    )
    if response.status_code == 200:
        print("Successfully uploaded to Zapier.")
    else:
        print("Failed to upload:", response.text)

# upload_to_make("karina_aespas_/2024-06-29_09-34-48_UTC.mp4", "video")