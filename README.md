# InstaGrabber

InstaGrabber is a Python script that allows you to download Instagram Reels using their URLs. The script uses `instaloader` to interact with Instagram and `pyfiglet` and `termcolor` to enhance the terminal experience with a stylish banner and colorful prompts.

## Features

- Download Instagram Reels using their URLs.
- Save Instagram session to avoid re-login.
- Stylish terminal interface with ASCII banner and colored prompts.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Required Python packages:
  - `instaloader`
  - `pyfiglet`
  - `termcolor`

You can install the required packages using pip:

```bash
pip install instaloader pyfiglet termcolor
```

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory containing the script.

3. Run the script:

```bash
python3 insta.py
```

4. Follow the prompts to enter your Instagram username and password, and the URL of the Instagram Reel you want to download.

## Script Details

When you run the script, you will see a banner and some additional information:

```
   ___           __        ____           __    
  / _ )___  ___ / /____   / __/__  ___ __/ /____
 / _  / _ \(_-</ __/ _ \ _\ \/ _ \/ _ `/ __/ -_)
/____/\___/___/\__/\___(_)_/\___/\_,_/\__/\__/

Developed by thisizasif
Launch Date: YYYY-MM-DD
Version: 1.0.0
```

After entering your Instagram credentials, you can enter the URL of the Instagram Reel you want to download. Once the download is complete, the script will ask if you want to download another Reel. You can continue downloading Reels or exit by choosing `n`.

## Note

- Ensure you have a stable internet connection while using this script.
- Your Instagram credentials are used only for logging in via `instaloader` and are not stored or shared.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or issues, please contact the developer at:

- GitHub: [thisizasif](https://github.com/thisizasif)
```

##Team thisizasif