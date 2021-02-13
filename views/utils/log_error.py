import logging


def logger(mensaje, exception):
    # Iniciamos cliente para logging
    logging.error(exception, exc_info=True)
