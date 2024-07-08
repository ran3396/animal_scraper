import requests
from bs4 import BeautifulSoup
import os
import logging

from downloader import Downloader
from utils import run_in_new_thread

class Scraper:
    def __init__(self, url: str, download_directory: str, logger: logging.Logger, download_images: bool = True):
        self.url = url
        self.download_directory = download_directory
        self.downloader = Downloader(download_directory, logger)
        self.download_images = download_images
        self.logger = logger


    def scrape(self):
        '''
        Scrape the Wikipedia page for animal adjectives and download corresponding images.
        Returns a dictionary with adjuctives as keys and a a dictionary that contains
        animals as keys and list of animals as values and images as keys and image path as values.
        '''
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the correct table under "Terms by species or taxon"
            header = soup.find(id='Terms_by_species_or_taxon')
            table = header.find_next('table', {'class': 'wikitable'})

            data = {}

            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                if len(columns) > 1:
                    animal = columns[0].find('a').text
                    adjectives = columns[5].decode_contents().split('<br/>')
                    animal_link = columns[0].find('a')
                    if '/' in animal:
                        # In case the image name contains a '/', replace it with an underscore because it's not a valid file name character
                        animal = animal.replace('/', '_')
                    if animal_link and self.download_images:
                        self._download_animal_image(animal_link, animal)
                    for adjective in adjectives:
                        adjective = adjective.strip()
                        if adjective not in data:
                            data[adjective] = {'animals': [animal], 'images': [os.path.join(self.download_directory, animal + '.jpg')]}
                        else:
                            data[adjective]['animals'].append(animal)
                            data[adjective]['images'].append(os.path.join(self.download_directory, animal + '.jpg'))

            return data
        except Exception as e:
            self.logger.exception(f"Failed to scrape data: {e}")
            return {}
    
    @run_in_new_thread
    def _download_animal_image(self, animal_link: BeautifulSoup, animel_name: str):
        '''
        Download the image of an animal from its Wikipedia page.
        We run this in a separate thread to speed up the process because downloading images can be slow.
        '''
        try:
            animal_url = 'https://en.wikipedia.org' + animal_link['href']
            animal_response = requests.get(animal_url)
            animal_soup = BeautifulSoup(animal_response.content, 'html.parser')
            # Images can sometimes be in a table or a figure tag
            if not animal_soup.find('table', {'class': 'infobox'}):
                img_tag = animal_soup.find('figure', {'class': 'mw-halign-right'}).find('img')
            else:
                img_tag = animal_soup.find('table', {'class': 'infobox'}).find('img')
            if img_tag:
                img_url = 'https:' + img_tag['src']
                self.downloader.download_image(img_url, animel_name)
            else:
                self.logger.warning(f"No image found for {animel_name}")
        except Exception as e:
            # Log the error and continue
            self.logger.exception(f"Failed to download image for {animel_name} because of an error: {e}")
