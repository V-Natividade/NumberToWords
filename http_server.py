import json
import re

from number_to_words import NumberToWords


class Server:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def format_number(self, number):
        return number.replace("/", "")

    def check_signal(self, number):
        return re.sub(r"-", "", str(number)) if "-" in number else number

    def __iter__(self):
        path = self.format_number(self.environ.get("PATH_INFO"))
        validator = self.check_signal(path)

        if validator.isnumeric():
            response_body = json.dumps(
                {"extenso": NumberToWords(path).convert()}, ensure_ascii=False
            ).encode("utf-8")
        else:
            response_body = bytes(
                "Inclua números cardinais e inteiros no path", "utf-8"
            )

        status = "200 OK"
        response_headers = [("Content-Type", "application/json")]
        self.start(status, response_headers)
        yield response_body
