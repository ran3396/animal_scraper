import unittest
import os
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper import Scraper
from downloader import Downloader
from html_generator import HTMLGenerator
from utils import read_config, setup_logging

class TestAnimalScraper(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.config = read_config('config/config.json')
        self.logger = setup_logging()

    def test_scrape(self):
        # Create a Scraper instance
        scraper = Scraper(self.config['url'], self.config['download_directory'], self.logger, download_images=False)

        # Test the scrape method
        data = scraper.scrape()

        # Check that the data is not empty
        self.assertTrue(data)

        # Check that the data contains the expected keys
        self.assertIn('Dolphin', data)

    def test_download_image(self):
        download_directory = self.config['download_directory']

        # Create a Downloader instance
        downloader = Downloader(download_directory, self.logger)
        
        # Test the download_image method
        downloader.download_image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tursiops_truncatus_01.jpg/250px-Tursiops_truncatus_01.jpg', 'image')

        # Check that the image exists in the download directory
        self.assertTrue(os.path.exists(os.path.join(download_directory, 'image.jpg')))

        # Clean up by deleting the downloaded image
        os.remove(os.path.join(download_directory, 'image.jpg'))

    def test_generate_html(self):
        # Create a sample data dictionary
        data = {
            'Dolphin': {'adjectives': ['delphine'], 'image': 'Dolphin.jpg'},
        }

        # Create an HTMLGenerator instance
        html_generator = HTMLGenerator(data, 'test.html', self.logger)

        # Test the generate method
        html_generator.generate()

        # Check that the HTML file exists on the path
        self.assertTrue(os.path.exists('test.html'))

        # Clean up by deleting the generated HTML file
        os.remove('test.html')

if __name__ == '__main__':
    unittest.main()