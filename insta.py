import instaloader
from getpass import getpass
import os
from termcolor import colored
from datetime import datetime
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("Insta-G")
    print(colored(banner, 'cyan'))

def colored_input(prompt, color='cyan'):
    return input(colored(prompt, color))

def download_instagram_reel():
    # Print the banner
    print_banner()

    # Additional information
    print(colored("Developed by thisizasif", 'yellow'))
    launch_date = datetime.now().strftime("%Y-%m-%d")
    print(colored(f"Launch Date: {launch_date}", 'yellow'))
    print(colored("Version: 1.0.0", 'yellow'))

    # Create an instance of the Instaloader class
    L = instaloader.Instaloader()

    # Define session file path
    session_file = 'insta_session'

    # Prompt for Instagram credentials if session file does not exist
    if os.path.exists(session_file):
        print(colored("Session file found. Using existing session.", 'green'))
        L.load_session_from_file(username=None, filename=session_file)
    else:
        username = colored_input("Enter your Instagram username: ", 'blue')
        password = getpass(colored("Enter your Instagram password: ", 'blue'))
        try:
            L.login(username, password)
            L.save_session_to_file(filename=session_file)
        except instaloader.exceptions.ConnectionException as e:
            print(colored(f"Failed to connect: {e}", 'red'))
            return
        except instaloader.exceptions.BadCredentialsException:
            print(colored("Invalid username or password.", 'red'))
            return

    while True:
        # Prompt for the Instagram Reel URL
        url = colored_input("Enter the Instagram Reel URL: ", 'yellow')

        # Extract the shortcode from the URL
        try:
            shortcode = url.split('/')[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target=f'reel_{shortcode}')
            print(colored("Download complete.", 'green'))
        except instaloader.exceptions.ProfileNotExistsException:
            print(colored("The provided URL is not valid or the profile does not exist.", 'red'))
        except instaloader.exceptions.InstaloaderException as e:
            print(colored(f"An error occurred: {e}", 'red'))

        # Ask if the user wants to download another reel
        choice = colored_input("Do you want to download another Instagram Reel? (y/n): ", 'yellow').strip().lower()
        if choice != 'y':
            break

# Run the function
if __name__ == "__main__":
    download_instagram_reel()