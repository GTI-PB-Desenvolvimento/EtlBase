import logging
from datetime import datetime
from pathlib import Path
from os import getenv



LOG_PATH = Path('logs')

def basic_logger(name):
    logger = logging.getLogger(name)

    try:
        log_level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARN,
            'error': logging.ERROR
        }[getenv('LOG_LEVEL', '')]

    except KeyError:
        log_level = 'warn'

    logger.setLevel(log_level)

    file_handler = logging.FileHandler(
        Path(LOG_PATH,f'{name}_{datetime.now().strftime('%Y%m%d')}.log'), 'a', 'utf-8'
    )
    stream_handler = logging.StreamHandler()

    for handler in (file_handler, stream_handler):
        handler.setFormatter(
            logging.Formatter(
                '%(asctime)s :: %(levelname)s :: %(module)s.%(funcName)s :: %(lineno)d :: %(message)s'
            )
        )
        logger.addHandler(handler)

    return logger
