#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse


class ChangeWords(object):

    @staticmethod
    def create_parser():
        """ return parsed args """
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description="Python tool to change or replace the text string in the files.")
        parser.add_argument(
            '-p', '--path', type=str,
            default='.', help="the file type you are looking for. eg: '.py', '.txt'\n"
                              "by default is current path/folder.")
        parser.add_argument(
            '-ft', '--file_type', type=str,
            default='.py', help="file type you are looking for, eg: '.py', '.txt'"
                                "by default is '.py' (python files)")
        parser.add_argument(
            '-fs', '--from_string',
            default=None, help="the string to change/replace")
        parser.add_argument(
            '-ts', '--to_string',
            default=None, help="the string replacement")
        return parser

    def change_words(self, search_path, file_type, from_str, to_str):
        """
        function to change or replace the text string in files.
        this function also implemented the recursive folders.

        :param `search_path` (String) => is current folder or parent folder for files.
        :param `file_type` (String) => is the file type you are looking for. eg: '.py', '.txt'
        :param `from_str` (String) => is the string to change/replace.
        :param `to_str` (String) => is the string replacement.

        return True
        """

        numb = 0
        for root, dirs, files in os.walk(os.path.normpath(search_path)):
            for filename in files:
                if filename.endswith(file_type):
                    numb += 1

                    # finding absolute file path
                    # eg: /home/username/tests/findwords/findwords.py
                    file_path = os.path.abspath(os.path.join(root, filename))
                    print('%s. %s' % (numb, file_path))

                    # reading file before replacement
                    file = open(file_path, 'r')
                    file_data = file.read()
                    file.close()

                    # replace the `from_str` to `to_str` for this file
                    new_data = file_data.replace(from_str, to_str)

                    # creating new file with same name
                    file = open(file_path, 'w')
                    file.write(new_data)
                    file.close()
        # noqa
        return True


def main():
    change = ChangeWords()
    parser = change.create_parser()
    args = parser.parse_args()

    if not args.from_string and not args.to_string:
        parser.print_help(sys.stderr)
        sys.exit(1)

    change.change_words(args.path, args.file_type,
                        args.from_string, args.to_string)

if __name__ == '__main__':
    main()
