import logging

# Create a logger and set the level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler for Pycharm and set the formatter
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

werkzeug_log = logging.getLogger('werkzeug')
werkzeug_log.setLevel(logging.ERROR)
