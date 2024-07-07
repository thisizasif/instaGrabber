import instaloader
from getpass import getpass
import os

def download_instagram_reel():
    # Create an instance of the Instaloader class
    L = instaloader.Instaloader()

    # Define session file path
    session_file = 'insta_session'

    # Prompt for Instagram credentials if session file does not exist
    if os.path.exists(session_file):
        print("Session file found. Using existing session.")
        L.load_session_from_file(username=None, filename=session_file)
    else:
        username = input("Enter your Instagram username: ")
        password = getpass("Enter your Instagram password: ")
        try:
            L.login(username, password)
            L.save_session_to_file(filename=session_file)
        except instaloader.exceptions.ConnectionException as e:
            print(f"Failed to connect: {e}")
            return
        except instaloader.exceptions.BadCredentialsException:
            print("Invalid username or password.")
            return

    # Prompt for the Instagram Reel URL
    url = input("Enter the Instagram Reel URL: ")

    # Extract the shortcode from the URL
    try:
        shortcode = url.split('/')[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=f'reel_{shortcode}')
        print("Download complete.")
    except instaloader.exceptionn:
        print("The provided URL is not valid or the profile does not exist.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    download_instagram_reel()
