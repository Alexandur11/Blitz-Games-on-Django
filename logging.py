import logging


class MaxLevelFilter(logging.Filter):

    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno < self.level


def setup_logging():
    file_cleanup('error_logs.txt')
    file_cleanup('info_logs.txt')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    custom_format = (
        "\n--------------------\n"
        "Timestamp: %(asctime)s\n"
        "Level: %(levelname)s\n"
        "Message: %(message)s\n"
        "--------------------\n"
    )

    # File handler for error logs (ERROR and CRITICAL messages)
    error_handler = logging.FileHandler("error_logs.txt")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(custom_format))
    logger.addHandler(error_handler)

    # File handler for info logs (INFO and lower severity messages)
    info_handler = logging.FileHandler("info_logs.txt")
    info_handler.setLevel(logging.DEBUG)
    info_handler.addFilter(MaxLevelFilter(logging.ERROR))
    info_handler.setFormatter(logging.Formatter(custom_format))
    logger.addHandler(info_handler)

    return logger


def file_cleanup(file):
    with open(file, 'w'):
        pass