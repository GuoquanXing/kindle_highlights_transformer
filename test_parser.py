import parser
from unittest.mock import MagicMock

file_contents = {'title': 'Kindle Notes and Highlights',
                 'contents': [{
                     'bookName': 'Tales of Two City', 
                     'notes': [{
                         'location': '- #3788-3789',
                          'timestamp': '9:42:07', 
                          'note': 'I Love You'}, 
                          {'location': '- #3790-3791', 
                          'timestamp': '9:43:07', 
                          'note': 'I Love You Too'}
                        ]}
                ]}

parser._read_file_in_lines = MagicMock(return_value = 
['Tales of Two City\r\n', 
    '- #3788-3789 | 9:42:07\r\n', 
    '\r\n', 
    'I Love You\r\n', 
    '==========', 
'Tales of Two City\r\n',
    '- #3790-3791 |  9:43:07\r\n',
    '\r\n', 
    'I Love You Too\r\n',
    '=========='])

def test_parser():
    assert parser.transform_notes_to_json("test.txt") == file_contents