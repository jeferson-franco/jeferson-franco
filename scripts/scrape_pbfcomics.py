import requests
from bs4 import BeautifulSoup
import os


def get_latest_pbf_comic():
    """
    Scrapes the latest comic image from pbfcomics.com and saves it locally.
    Returns the filename of the saved image.
    """
    try:
        # Send request to the website
        response = requests.get("https://pbfcomics.com/")
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the image element by looking for the first article's image
        article = soup.find("article")
        if article:
            img_element = article.find("img")
            if img_element and "src" in img_element.attrs:
                img_url = img_element["src"]
                if img_url.startswith("data:image"):
                    print(
                        "Found a data URI instead of an image URL. Checking for 'data-src' attribute."
                    )
                    if "data-src" in img_element.attrs:
                        img_url = img_element["data-src"]
                    else:
                        print("No valid image URL found in 'data-src' attribute.")
                        return None

                img_name = os.path.basename(img_url)

                # Download the image
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                # Save the image locally
                local_filename = f"latest_pbf_cartoon.jpg"
                with open(local_filename, "wb") as f:
                    f.write(img_response.content)

                print(f"Successfully downloaded {img_name} as {local_filename}")
                return local_filename
            else:
                print("No image found in the first article.")
                return None
        else:
            print("No article found on the page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the comic: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


if __name__ == "__main__":
    get_latest_pbf_comic()
