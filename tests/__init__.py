import os
import unittest

from python_hosts import parse_file, build_file, parse_string


class BaseTest(unittest.TestCase):

    def test_parse_file_1(self):
        data = parse_file(os.path.normpath(os.path.join(os.path.dirname(__file__), 'data', 'hosts-simple')))
        self.assertListEqual\
            ( data
            , [ '# wrong config'
              , ('127.0.0.1', {'localhost', })
              , '# proper config'
              , ('127.0.0.1', {'node1.localhost', 'node.local', 'localhost'})
            ] )

    def test_parser_string_1(self):
        v = b"""127.0.0.1 localhost"""
        self.assertListEqual(parse_string(v), [('127.0.0.1', {'localhost', })])

    def test_build_1(self):
        data = parse_file(os.path.normpath(os.path.join(os.path.dirname(__file__), 'data', 'hosts-simple')))
        content = build_file(data)
        compare = """# wrong config
127.0.0.1	localhost
# proper config
127.0.0.1	node1.localhost node.local localhost"""
        self.assertEqual(content, compare)