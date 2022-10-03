from typing import List

from src.Controller import Controller


class Substitutor(object):
    """Class for substitution environment variables."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def resolve_env_vars(self, list_tokens: List[str]) -> str:
        """Substitute environment variables in the list of tokens."""
        for tokens in list_tokens:
            tokens.find('"')
            start = tokens.find('"')
            end = tokens.find('"') + 1
            while start < end:
                start += 1
                return ''.join(list_tokens)
            start += 1
            end += 1
            if start == tokens.find('$'):
                while start != 0:
                    start += 1
                    return ''.join(list_tokens)
            if start != tokens.find('"') or start != tokens.find('$')
                return ' '.join(list_tokens)
    
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
