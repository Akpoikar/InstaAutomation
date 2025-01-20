import PostDownloader
import time
import bb
import os
import make
import shutil
def get_files(directory, ending):
    try:
        all_files = os.listdir(directory)
        
        files = [file for file in all_files if file.endswith(ending)]
        
        return files
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def hasVideo(directory):
    files = get_files(directory, ".mp4")
    return len(files) > 0

def upload(username, fileNames):
    results = []
    for file in fileNames:
        result = bb.upload_to_imgbb(username + '/' +file)
        print(result)
        results.append(result)
    print(results)
    return results

def getTextFromFile(caption_file):
    with open(caption_file, "r", encoding="utf-8") as file:
        content = file.read() 
        return content
    
username = ""  # Replace with the Instagram username
with open("conf.txt", "r") as file:
        # Read the content of the file
        username = file.readline().strip()  # Read the first line and remove leading/trailing whitespace

while True:
   
    shutil.rmtree(username)

    post_detected = PostDownloader.check_for_new_posts(username)
    if post_detected is False:
        time.sleep(600)
        print("Didnt find anything")
        continue
    caption_file = get_files(username,".txt")[0]
    caption = getTextFromFile(username + '/' + caption_file)
    
    fileNames = []
    VideoFlag = False
    if hasVideo(username):
        VideoFlag = True
        fileNames = get_files(username, ".mp4")
        print('Video type is detected')
    else:
        fileNames = get_files(username, ".jpg")
        # fileNames = get_files(username, ".webp")
    
    file_urls = []

    if VideoFlag:
        result = bb.upload_video_to_vk(username + '/' + fileNames[0], title=fileNames[0])
        file_urls.append(result["url"])
    else:
        file_urls = upload(username, fileNames)

    if len(file_urls) > 1:
        make.upload_to_make_multiple(file_urls,'carousel',caption=caption)
    else:
    #TODO: switch case
        for url in file_urls:
            if VideoFlag :
                continue
                make.upload_to_make(url,"video", caption=caption)
            else:
                make.upload_to_make(url,"photo", caption=caption)


    time.sleep(600)