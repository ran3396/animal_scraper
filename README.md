# Web Scraper

This project is a web scraping application designed to scrape collateral adjectives and animals from the Wikipedia page on animal names. It also downloads images of the animals and generates an HTML file with the results.

## Directory Structure

```commandline
animal_scraper/
├── config/
│   └── config.json
├── src/
│   ├── main.py
│   ├── scraper.py
│   ├── downloader.py
│   ├── utils.py
│   └── html_generator.py
├── tests/
│   ├── test_animal_scraper.py
├── requirements.txt
├── README.md
```


## Configuration

The application uses a JSON configuration file located at `config/config.json`. Update this file with the desired configuration.

## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ran3396/animal_scraper.git
    cd animal_scraper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the main script:
    ```sh
    python src/main.py
    ```

2. The results will be saved by default in `output/result.html`.

## Running Tests

1. Navigate to the `tests` directory and run the test scripts:
    ```sh
    cd tests
    python -m unittest .\\test\\test_animal_scraper.py
    ```