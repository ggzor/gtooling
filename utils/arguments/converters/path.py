from pathlib import Path
from os import mkdir, rmdir
from tempfile import TemporaryFile
from utils.languageex import value_or_raise_if

class validate:
    @staticmethod
    def existing(path):
        return value_or_raise_if(
            not path.exists(), 
                "The path '{}' doesn´t exist.".format(path), 
            path
        )

    @staticmethod
    def isdirectory(path):
        return value_or_raise_if(
            not path.is_dir(),
                "The path '{}' is not a directory.".format(path),
            path
        )

    @staticmethod
    def valid_directoryname(name):
        try:
            mkdir(name)
            p = Path(name)

            if p.is_dir():   
                rmdir(name)
                return name
        except:
            raise Exception("The value '{}' is not a valid directory name.".format(name))