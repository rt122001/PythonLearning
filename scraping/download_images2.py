import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random

# Function to download a single image
def download_image(url, folder_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Extract the image file name
        #image_name = url.split("/")[-1]
        image_name=str(random.randint(0,1000)) + ".png"
        save_path = os.path.join(folder_path, image_name)
        
        # Save the image to the specified path
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Image successfully downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image {url}: {e}")

# Function to download all images from a webpage
def download_all_images_from_webpage(webpage_url, folder_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(webpage_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        img_tags = soup.find_all('img')
        img_urls = [img.get('src') for img in img_tags if img.get('src')]
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Download each image
        for img_url in img_urls:
            # Handle relative URLs
            full_img_url = urljoin(webpage_url, img_url)
            download_image(full_img_url, folder_path)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Example usage
webpage_url = 'https://dpssl.net/all-alumni.php'  # Replace with the actual webpage URL
folder_path = 'downloaded_images'    # Folder where images will be saved

download_all_images_from_webpage(webpage_url, folder_path)
