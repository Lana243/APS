from typing import Optional, List, Tuple
import os

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class LsCommand(Command):
    """Class representing ls command"""

    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('ls', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        try:
            directory = None if len(self.args) == 0 else self.args[0].data
            result = '\n'.join(os.listdir(directory))
        except Exception as exp:
            return '', str(exp), -1
        return result, '', 0
