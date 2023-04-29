import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def log(text):
    logger.info(text)
