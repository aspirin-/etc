import logging

LOGGING_FORMAT = '%(levelname)s: %(funcName)s | %(message)s'


def generic_logger():
    """Just in case a mistake is made, classes can use this generic logger."""
    logger = logging.getLogger("cli_logger")
    logger.setLevel(logging.DEBUG)

    return logger


def make_logging(debug, verbose, quiet):
    """Set up logging and level of verbosity"""
    logger = logging.getLogger("cli_logger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOGGING_FORMAT)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    if debug:
        ch.setLevel(logging.DEBUG)
    elif verbose:
        ch.setLevel(logging.INFO)
    elif quiet:
        ch.setLevel(logging.CRITICAL)

    if not debug and not verbose and not quiet:
        ch.setLevel(logging.WARNING)

    logger.addHandler(ch)
    logger.info('Verbosity set.')
    return logger


def main():
    """Example function"""
    logger = make_logging(debug=True, verbose=False, quiet=False)
    logger.debug("This is an example of basic logging.")
    logger.info("This is info-level.")
    logger.warning("Warning-level.")
    logger.error("This is an error-level log.")
    logger.critical("It's critical!")

    try:
        logger * 2
    except Exception as e:
        logger.exception("And this is an exception log. Traceback:")

    logger.debug("The program continues.")

if __name__ == '__main__':
    main()
