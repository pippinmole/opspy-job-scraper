import logging

logger = logging
logger.basicConfig(
    format='%(asctime)s [%(levelname)s] [%(name)s] - [%(funcName)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
