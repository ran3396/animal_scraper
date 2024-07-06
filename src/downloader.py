import requests
import os
import logging

from utils import ensure_directory


class Downloader:
    def __init__(self, download_directory: str, logger: logging.Logger):
        self.download_directory = download_directory
        ensure_directory(download_directory)
        self.logger = logger

    def download_image(self, image_url: str, image_name: str):
        # Download an image and save it to the specified directory.
        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                file_name = os.path.join(self.download_directory, f"{image_name}.jpg")
                with open(file_name, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                self.logger.info(f"Downloaded image: {file_name}")
        except Exception as e:
            self.logger.exception(f"Failed to download image: {image_url} because of an error: {e}")
