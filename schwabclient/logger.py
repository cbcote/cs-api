# logger.py
import logging
from logging.handlers import RotatingFileHandler
import os

# Define the default logger
logger = logging.getLogger(__name__)

# Set the default logging level, e.g., DEBUG, INFO, WARNING, ERROR, or CRITICAL
logger.setLevel(logging.INFO)

# Define formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# File handler for logging to a file that rotates when the file reaches 1MB with a maximum of 5 backup files
file_handler = RotatingFileHandler('api_client.log', maxBytes=1024*1024, backupCount=5)
file_handler.setFormatter(formatter)

# Stream handler for logging to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def set_logging_level(level_name):
    """
    Set the logging level for the logger.
    
    Args:
        level_name (str): The name of the logging level.
    
    Raises:
        ValueError: If the logging level name is invalid.
    """
    level_name = level_name.upper()
    if level_name not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        raise ValueError(f'Invalid logging level: {level_name}')
    level = getattr(logging, level_name)
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)

# Define other utility functions related to logging if needed.
