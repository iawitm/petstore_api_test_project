import logging
from requests import Response


def info_logging(response: Response):
    logging.info(f"URL: {response.request.url}")
    logging.info(f"Method: {response.request.method}")
    if response.request.body:
        logging.info(f"Request body: {response.request.body}")
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Response text: {response.text}")
