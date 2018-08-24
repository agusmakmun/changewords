===================
changewords
===================

|pypi version| |build status|

Simply python tool to change or replace the strings in files.
This tool pretty nice for programmers if somehow they want to replace/change their codes for any files,
eg: ``function``, ``class``, ``variable``, etc for recursive files or not.


Installation
============

Install from PyPI:

::

    $ pip install changewords


Usage
--------------

::

    usage: changewords.py [-h] [-p PATH] [-ft FILE_TYPE] [-fs FROM_STRING]
                          [-ts TO_STRING]

    Python tool to change or replace the strings in files.

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  the file type you are looking for. eg: '.py', '.txt'
                            by default is current path/folder.
      -ft FILE_TYPE, --file_type FILE_TYPE
                            file type you are looking for, eg: '.py', '.txt'
      -fs FROM_STRING, --from_string FROM_STRING
                            the string to change/replace
      -ts TO_STRING, --to_string TO_STRING
                            the string replacement


Example
--------------

::

    $ changewords -p=changewords_test -ft=.py -fs=helloworld -ts=mantabjiwa

    # or

    $ changewords --path=changewords_test --file_type=.py --from_string=helloworld --to_string=mantabjiwa



Running tests
--------------

To run the test use:

::

    $ python tests.py


.. |pypi version|
   image:: https://img.shields.io/pypi/v/changewords.svg
   :target: https://pypi.python.org/pypi/changewords

.. |build status| image:: https://travis-ci.org/agusmakmun/changewords.svg?branch=master
   :target: https://travis-ci.org/agusmakmun/changewords
