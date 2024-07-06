import logging

class HTMLGenerator:
    def __init__(self, data: dict, output_file: str, logger: logging.Logger):
        self.data = data
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
                <tr><th>Animal</th><th>Collateral adjective</th><th>Image</th></tr>
            """

            for animel in self.data:
                img_tag = f'<img src="{self.data[animel]["image"]}" alt="{animel}">' if self.data[animel]["image"] else ''
                html_content += f"<tr><td>{animel}</td><td>{self.data[animel]['adjectives']}</td><td>{img_tag}</td></tr>"

            html_content += """
            </table>
            </body>
            </html>
            """
        except Exception as e:
            self.logger.exception(f"Failed to generate HTML content: {e}")
            return

        try:
            with open(self.output_file, 'w') as file:
                file.write(html_content)
                self.logger.info(f"HTML file generated: {self.output_file}")
        except IOError as e:
            self.logger.exception(f"Failed to write HTML file: {e}")
