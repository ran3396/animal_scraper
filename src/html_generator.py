import logging
import os

from utils import ensure_directory

class HTMLGenerator:
    def __init__(self, data: dict, output_file: str, logger: logging.Logger):
        self.data = data
        ensure_directory(os.path.dirname(output_file))
        self.output_file = output_file
        self.logger = logger

    def generate(self):
        try:
            html_content = """
            <html>
            <head><title>Animal Adjectives</title></head>
            <body>
            <h1>Animal Adjectives</h1>
            <table border="1">
                <tr><th>Collateral adjective</th><th>Animals</th><th>Images</th></tr>
            """

            for adjuctive in self.data:
                # The dictionary looks like this: {'adjective': {'animals': ['animal1', 'animal2'], 'images': ['image1', 'image2']}}
                # We want to create a table row for each adjective with the corresponding list of animals and list of images
                image_tags = [f'<img src="{image}" alt="{animal}">' for animal, image in zip(self.data[adjuctive]['animals'], self.data[adjuctive]['images'])]
                html_content += f"<tr><td>{adjuctive}</td><td>{self.data[adjuctive]['animals']}</td><td>{''.join(image_tags)}</td></tr>"

            html_content += """
            </table>
            </body>
            </html>
            """

            self.logger.info(f"HTML file generated at {self.output_file}")
            
        except Exception as e:
            self.logger.exception(f"Failed to generate HTML content: {e}")
            return

        try:
            with open(self.output_file, 'w') as file:
                file.write(html_content)
                self.logger.info(f"HTML file generated: {self.output_file}")
        except IOError as e:
            self.logger.exception(f"Failed to write HTML file: {e}")
