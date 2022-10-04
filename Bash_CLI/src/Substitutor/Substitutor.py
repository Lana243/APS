from typing import List

from src.Controller import Controller


class Substitutor(object):
    """Class for substitution environment variables."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def resolve_env_vars(self, list_tokens: List[str]) -> str:
        """Substitute environment variables in the list of tokens."""
        inside_bracket = False
        string = ''
        for tokens in list_tokens:
            """Сhecking the values in the list of tokens."""
            if tokens == '"':
            """Сonditions for the double quote token"""
                result = tokens
                inside_bracket = not inside_bracket
            elif tokens.startswith('$'):
            """Сonditions for the token with variable input"""
                var_name = tokens[1:]
                if var_name in self.controller.env_vars:
                    var_name = self.controller.env_vars[var_name]
                result = var_name 
            if inside_bracket:
                separator = ''
            else:
                separator = ' '
            string += separator + result
        """Assembly and output of the received string"""
        return string

    # def resolve_env_var(self, list_tokens, mapper: Controller[str]) -> str:
    #     """
    #     Основной метод подстановки.
    #     """
    #     def replace(new_tok: Controller[str]) ->str:
    #         for tokens in list_tokens:
    #             """
    #             Проходится по массиву токенов
    #             после разбора строки лексера.
    #             """
    #             if len(tokens) == 1 and tokens == '$':
    #                 new_token = new_tok.group(1)
    #                 new_token_value = mapper.get(new_token, '')
    #                 """
    #                 Осуществляет подстановку переменных в токены,
    #                 заменяет все токены на строки
    #                 """
    #                 return new_token_value
    #     return re.sub(r'\$', replace, self)
