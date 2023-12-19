import logging
import logging.handlers
from datetime import datetime
from pathlib import Path
from os import getenv

from .mail import SMTPConfig


LOG_PATH = Path('logs')


def setup_logger(name, *handlers):
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

    for handler in [file_handler, stream_handler, *handlers]:
        handler.setFormatter(
            logging.Formatter(
                '%(asctime)s :: %(levelname)s :: %(module)s.%(funcName)s :: %(lineno)d :: %(message)s'
            )
        )
        logger.addHandler(handler)

    return logger

def setup_email_handler(name, smtp_config: SMTPConfig, toaddrs: list[str]):
    return logging.handlers.SMTPHandler(
        mailhost=(smtp_config.host, smtp_config.port),
        fromaddr=smtp_config.email,
        toaddrs=toaddrs,
        subject=name,
        credentials=(smtp_config.email, smtp_config.password)
    )
