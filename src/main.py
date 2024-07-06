from scraper import Scraper
from html_generator import HTMLGenerator
from utils import read_config, setup_logging

def main():
    # First, we read the configuration file and set up the logger.
    config = read_config('config/config.json')
    logger = setup_logging()

    # Next, we create an instance of the Scraper class and call the scrape method to get the data
    scraper = Scraper(config['url'], config['download_directory'], logger)
    data = scraper.scrape()

    # Finally, we create an instance of the HTMLGenerator class and call the generate method to create the HTML file
    if data:
        html_generator = HTMLGenerator(data, config['output_html'], logger)
        html_generator.generate()

if __name__ == "__main__":
    main()
