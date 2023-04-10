# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app.core.messages.schema.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

from core.tools.threading_mode import run_in_background
from typing import Any, Callable

from cache.redis_connect import Cache

from views.start.start.exec_ import StartChatExec
StartChatExec_ = StartChatExec()

from views.start.help.exec_ import HelpChatExec
HelpChatExec_ = HelpChatExec()

from views.start.open_account.exec_ import OpenAccountChatExec
OpenAccountChatExec_ = OpenAccountChatExec()


class FIRST_EXEC:
    @staticmethod
    def first_commands(data: dict[str, Any]) -> None:
        commands_function: list[Callable[[dict[str, str]], None]] = [
            StartChatExec_.exec_,
            HelpChatExec_.exec_,
            OpenAccountChatExec_.exec_,
        ]
        
        for execute_ in commands_function:
            run_in_background(execute_, (data,))
    
    @staticmethod
    def open_account_command(chat_id: int, data: dict[str, Any]) -> None:
        run_in_background(OpenAccountChatExec_.exec_in_cache, (data,))
        if Cache.TalkMode.log_in_branch.get(chat_id):
            Cache.TalkMode.open_account_branch.delete(chat_id)