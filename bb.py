import requests
import os
# === CONFIGURATION ===
IMGBB_API_KEY = "54186a42bc4685e9874e49ab62c46c08"  # Replace with your ImgBB API key

# === Upload Image to ImgBB ===
def upload_to_imgbb(image_path):
    print("Uploading image to ImgBB...")
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMGBB_API_KEY,  # Your ImgBB API key
    }
    files = {
        "image": open(image_path, "rb"),  # Open the image file in binary mode
    }

    response = requests.post(url, data=payload, files=files)
    
    # Check if upload was successful
    if response.status_code == 200:
        img_url = response.json()["data"]["url"]
        print(f"Image uploaded successfully! URL: {img_url}")
        return img_url
    else:
        print(f"Failed to upload image to ImgBB: {response.json()}")
        return None
    
ACCESS_TOKEN = 'N4DAhPO8QwiNi0J1OzXCc121fYFvoBN9'  # Replace with your Vimeo access token



# Replace with your VK access token
ACCESS_TOKEN = "1ac4fd561ac4fd561ac4fd56a419e330be11ac41ac4fd567d4ad2e32e7fa192807a8686"
API_VERSION = "5.131"
GROUP_ID = None  # Use if uploading to a group; otherwise, set to None

def upload_video_to_vk(video_path, title="My Video", description="Video description"):
    try:
        # Step 1: Get the upload URL
        params = {
            "access_token": ACCESS_TOKEN,
            "v": API_VERSION,
            "name": title,
            "description": description,
            "group_id": GROUP_ID,  # Optional: for uploading to a group
        }
        response = requests.get("https://api.vk.com/method/video.save", params=params)
        response_data = response.json()

        if "error" in response_data:
            raise Exception(f"Error from VK API: {response_data['error']['error_msg']}")

        upload_url = response_data["response"]["upload_url"]

        # Step 2: Upload the video
        with open(video_path, "rb") as video_file:
            files = {"video_file": video_file}
            upload_response = requests.post(upload_url, files=files)

        upload_result = upload_response.json()
        if "error" in upload_result:
            raise Exception(f"Error during video upload: {upload_result['error']}")

        print("Video uploaded successfully:", upload_result)
    except Exception as e:
        print("An error occurred:", e)

