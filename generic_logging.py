#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
When writing a package, set up generic logging by importing 'logging', then use
logging.info() (, etc.). 

import logging

class Genera(object):
    def __init__(self):
        logging.info('initializing Genera')

"""

import logging

from logzero import LogFormatter as _lzlf

LOGFILE_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'


def make_logger(logfile: str = '', loglevel: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger()

    if logfile:
        fh_handler = logging.FileHandler(logfile)
        # set logging level for file handler
        fh_handler.setLevel(logging.DEBUG)
        fh_handler.setFormatter(
            logging.Formatter(LOGFILE_FORMAT))
        logger.addHandler(fh_handler)

    ch_handler = logging.StreamHandler()
    ch_handler.setFormatter(_lzlf())
    ch_handler.setLevel(loglevel)  # set logging level for console handler
    logger.addHandler(ch_handler)
    logger.setLevel(logging.DEBUG)  # set overall logging level

    logger.info("Logging set up.")

    if logfile:
        logger.info("Logfile: {}".format(logfile))

    return logger


def main():
    """Example function"""
    logger = make_logger(
        logfile='/tmp/generic_logging.py.log', loglevel=logging.DEBUG)
    logger.debug("This is an example of basic logging.")
    logger.info("This is info-level.")
    logger.warning("Warning-level.")
    logger.error("This is an error-level log.")
    logger.critical("It's critical!")

    try:
        logger * 2
    except Exception:
        logger.exception("Exception! Cannot multiply 'logging.Logger'. Traceback:")

    logger.debug("The program continues.")


if __name__ == '__main__':
    main()
