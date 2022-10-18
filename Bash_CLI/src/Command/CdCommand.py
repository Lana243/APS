from typing import Optional, List, Tuple
import os

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class CdCommand(Command):
    """Class representing cd command"""

    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('cd', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        try:
            directory = os.path.expanduser("~") if len(self.args) == 0 else self.args[0].data
            os.chdir(directory)
        except Exception as exp:
            return '', str(exp), -1
        return '', '', 0
