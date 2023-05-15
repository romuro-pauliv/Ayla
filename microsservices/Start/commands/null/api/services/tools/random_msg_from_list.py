# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                         api.services.tools.random_msg_from_list.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from random import randint
from typing import Union
# |--------------------------------------------------------------------------------------------------------------------|


def random_msg_from_list(msg_list: list[str]) -> Union[str, list[str]]:
    index: int = randint(0, (len(msg_list)-1))
    return msg_list[index]