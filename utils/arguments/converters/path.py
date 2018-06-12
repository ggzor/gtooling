from pathlib import Path
from utils.languageex import value_or_raise_if

class validate:
    @staticmethod
    def existing(path):
        return value_or_raise_if(
            not path.exists(), 
                'The path "{}" doesn´t exist.'.format(path), 
            path
        )

    @staticmethod
    def isdirectory(path):
        return value_or_raise_if(
            not path.is_dir(),
                'The path "{}" is not a directory.'.format(path),
            path
        )