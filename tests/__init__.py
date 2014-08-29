import os
import unittest

from python_hosts import parse_file, build_file


class BaseTest(unittest.TestCase):

    def test_parse_1(self):
        data = parse_file(os.path.normpath(os.path.join(os.path.dirname(__file__), 'data', 'hosts-simple')))

    def test_build_1(self):
        data = parse_file(os.path.normpath(os.path.join(os.path.dirname(__file__), 'data', 'hosts-simple')))
        print build_file(data)