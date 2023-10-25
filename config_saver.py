"""for managing configs and storing as json

    Raises:
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
"""

import os
import json

class Config:
    """
    A class to handle configuration variables
    """
    def __init__(self, savefile) -> None:
        self.globals: dict = {}
        self.savefile = savefile

    def add_global(self,
                   key:str,
                   value=None):
        """
        Adds a variable to the list
        """
        self.globals[key] = value

    def save_globals(self):
        """
        Saves globals to the savefile
        """
        if not os.path.exists(os.path.dirname(self.savefile)):
            os.makedirs(os.path.dirname(self.savefile))
        with open(self.savefile, 'w', encoding='utf-8') as file:
            json.dump(self.globals, file, indent=4)

    def load_globals(self):
        if os.path.exists(self.savefile):
            with open(self.savefile, 'r', encoding='utf-8') as f:
                self.globals = json.load(f)
        else:
            raise FileNotFoundError

    def read_globals(self):
        """
        Lets the user define the the globals
        """
        print("You will have to define some settings")
        for key, value in self.globals.items():
            if value is None:
                self.globals[key] = input(f"{key}=")

    def __getitem__(self,
                    key):
        return self.globals[key]

    def __setitem__(self,
                    key,
                    value):
        self.globals[key] = value

    def __delitem__(self, key):
        del self.globals[key]
