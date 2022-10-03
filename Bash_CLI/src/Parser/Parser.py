from typing import List

from src.Controller import Controller


class Parser(object):
    """Class for splitting the list of tokens into separate commands."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def parse_commands(self, list_tokens: List[str]) -> List[List[str]]:
        """Split list_tokens into separate commands."""
        for tokens in list_tokens:
            tokens.find('|')
            start = tokens.find('|')
            if start == tokens.find('|'):
                yield list_tokens # пока не решила как поделить массив
        return [list_tokens]

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
