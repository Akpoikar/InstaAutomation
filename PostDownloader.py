import instaloader

loader = instaloader.Instaloader()
last_seen_post_time = None

def DownloadLatestPost(username):
    # Initialize instaloader instance


    # Specify the username to download the latest post from

    profile = instaloader.Profile.from_username(loader.context, username)
    try:
        latest_post = next(profile.get_posts())

        # Download the latest post
        print(f"Downloading the latest post of @{username}...")
        loader.download_post(latest_post, target=username)
        print("Latest post downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

def check_for_new_posts(username):
    global last_seen_post_time
    latest_post = get_latest_post(username)

    if latest_post:
        # Check if the post is new
        if last_seen_post_time is None or latest_post.date_utc > last_seen_post_time:
            print(f"New post detected! {latest_post.url}")
            last_seen_post_time = latest_post  # username the timestamp
            loader.download_post(last_seen_post_time, target=username)
            return True
    return False

def get_latest_post(username):
    profile = instaloader.Profile.from_username(loader.context, username)
    # Get the latest username
    return next(profile.get_posts())