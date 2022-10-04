from typing import List

from src.Controller import Controller


class Parser(object):
    """Class for splitting the list of tokens into separate commands."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def parse_commands(self, list_tokens: List[str]) -> List[List[str]]:
        """Split list_tokens into separate commands."""
        solid = []
        line = []
        for tokens in list_tokens:
        """Сhecking the values in the list of tokens."""
            if tokens == '|':
            """Сonditions for the vertical line token"""    
                solid.append(line)
                line = []
            else:
                line.append(tokens)
            while True:
            """Dividing list_tokens in the presence of a vertical line token"""
                try:
                    solid.remove([])
                except ValueError:
                    break
        return solid

    # def parse_commands(self, list_tokens) -> str:
    #     """
    #     Принимает список токенов.
    #     """
    #     for tokens in list_tokens:
    #         if len(tokens) == 1 and tokens[0]:
    #             token = tokens[0]
    #             name, value = [arg.strip() for arg in token.string.split("=")]
    #             arg_name = tokens(tokens.str, name)
    #             arg_value = tokens(tokens.str, name.strip('\"').strip('\''))
    #             """
    #             # Представляет обычный массив,
    #             который просто выдаёт объекты класса.
    #             """
    #     return Controller(Parser(name, [arg_name, arg_value]))
