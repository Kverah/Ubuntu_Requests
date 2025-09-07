import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    # Prompt user for URL
    url = input("Enter the image URL: ").strip()
    
    # Directory for storing fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError if the request was unsuccessful

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no valid filename, generate one
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"

        # Full path for saving
        filepath = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully saved at: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ The request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
