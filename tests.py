#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from changewords.change_words import ChangeWords


class ChangeWordsTestCase(unittest.TestCase):
    """Tests for `changewords/change_words.py`."""

    def setUp(self):
        change = ChangeWords()
        self.parser = change.create_parser()
        self.change_words = change.change_words

    def test_is_words_changed(self):
        pa = self.parser.parse_args(['--path', 'changewords_test'])
        ft = self.parser.parse_args(['--file_type', '.py'])
        fs = self.parser.parse_args(['--from_string', 'helloworld'])
        ts = self.parser.parse_args(['--to_string', 'mantabjiwa'])

        self.assertTrue(self.change_words(pa.path, ft.file_type,
                                          fs.from_string, ts.to_string))

if __name__ == '__main__':
    unittest.main()
