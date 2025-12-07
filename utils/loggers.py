import logging
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'logs', 'errors.log')
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def log_error(message):
    logging.error(message)
