# write test for schwabclient module

import unittest
from schwabclient.client import APIClient
import os
import logging
from logging.handlers import RotatingFileHandler
from schwabclient.logger import set_logging_level

class TestSchwabClient(unittest.TestCase):
    """
    Test the SchwabClient class.
    """
    def set_up(self):
        """
        Set up the SchwabClient object for testing.
        """
        self.client = APIClient()