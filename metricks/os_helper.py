__author__ = 'khomitsevich'

import os
import sys

class OSHelper:
    """ Helper class has several methods which operate `os` system library. """

    @staticmethod
    def validateInputArgumentsAmount(argv: list):
        if len(argv) > 2:
            print("Input shouldn't has more than 1 input argument. Try again.")
            sys.exit(1)

    @staticmethod
    def validateInputArgumentAsDirectory(dirpath: str):
        if not isDirectoryPathExists(dirpath):
            print("Current argument is not a valid as directory path. Try again.")
            sys.exit(1)

    @staticmethod
    def getCurrentDirectory():
        return os.getcwd()


# Private method `isDirectoryPathExists`
def isDirectoryPathExists(path: str):
        return os.path.exists(os.path.dirname(path))
