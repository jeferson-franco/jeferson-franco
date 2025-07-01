#!/usr/bin/env python3
"""
Script to scrape the latest cartoon from Explosm.net (Cyanide & Happiness)
and save it with a static filename. This script is designed to be educational
and easy to understand for beginners learning web scraping with Python.
"""

import requests
from bs4 import BeautifulSoup
import os


def get_latest_cartoon_url():
    """
    Fetch the Explosm.net homepage and extract the URL of the latest comic image.
    Returns the image URL as a string or None if extraction fails.
    """
    # URL of the Explosm website
    url = "http://explosm.net"

    # Set a user-agent to mimic a browser request, reducing the chance of being blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Send HTTP GET request to the website
        response = requests.get(url, headers=headers, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return None

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the latest comic image element
        # Note: This selector might need adjustment if the website structure changes
        # Trying to find the comic image by ID or class related to comics
        comic_img = soup.find("img", id="main-comic")
        if not comic_img:
            # Fallback to searching for images in a comic container or with specific class
            comic_container = soup.find("div", class_="comic-container") or soup.find(
                "div", id="comic-container"
            )
            if comic_container:
                comic_img = comic_container.find("img")
            else:
                # Last resort: look for any image with keywords related to comics or dates in the src
                # Explosm might use naming conventions like 'comic', 'cnh', 'cyanide', or date patterns
                for img in soup.find_all("img"):
                    if "src" in img.attrs:
                        src_lower = img["src"].lower()
                        if any(
                            keyword in src_lower
                            for keyword in ["comic", "cnh", "cyanide", "daily", "strip"]
                        ):
                            comic_img = img
                            break
                        # Check for date patterns in the URL (e.g., '2023', '2024', etc.)
                        elif any(
                            year in src_lower for year in ["2023", "2024", "2025"]
                        ):
                            comic_img = img
                            break

        if comic_img and "src" in comic_img.attrs:
            # Ensure the src is a full URL
            img_url = comic_img["src"]
            if not img_url.startswith("http"):
                img_url = (
                    "http:" + img_url
                    if img_url.startswith("//")
                    else f"http://explosm.net{img_url}"
                )
            return img_url
        else:
            print(
                "Could not find the latest comic image on the page. Website structure may have changed."
            )
            # Debug: Print potential image elements for diagnosis
            images = soup.find_all("img")[:5]  # Limit to first 5 for brevity
            if images:
                print("Debug - Potential image elements found:")
                for i, img in enumerate(images, 1):
                    src = img.get("src", "No src")
                    alt = img.get("alt", "No alt")
                    img_id = img.get("id", "No id")
                    img_class = img.get("class", "No class")
                    print(
                        f"  {i}. src: {src}, alt: {alt}, id: {img_id}, class: {img_class}"
                    )
            else:
                print("Debug - No image elements found on the page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while parsing webpage: {e}")
        return None


def download_image(img_url, output_filename):
    """
    Download the image from the given URL and save it with the specified filename.
    Returns True if successful, False otherwise.
    """
    try:
        # Set user-agent for the image request as well
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send HTTP GET request to download the image
        response = requests.get(img_url, headers=headers, timeout=10)

        if response.status_code == 200:
            # Write the image content to a file, overwriting any existing file
            with open(output_filename, "wb") as f:
                f.write(response.content)
            print(f"Successfully downloaded and saved image as {output_filename}")
            return True
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error while saving image: {e}")
        return False


def main():
    """
    Main function to orchestrate the scraping and downloading process.
    """
    print("Starting script to scrape the latest Explosm cartoon...")

    # Get the URL of the latest cartoon image
    img_url = get_latest_cartoon_url()

    if img_url:
        print(f"Found latest cartoon image URL: {img_url}")
        # Define the static filename for the output image
        output_filename = "latest_explosm_cartoon.jpg"
        # Download and save the image
        success = download_image(img_url, output_filename)
        if not success:
            print("Failed to download or save the image.")
    else:
        print("Failed to extract the latest cartoon image URL.")

    print("Script execution completed.")


if __name__ == "__main__":
    main()
