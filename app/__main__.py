# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app.__main__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from typing import Any
from cache.redis_connect import Cache
from core.messages.schema import FIRST_EXEC
# |--------------------------------------------------------------------------------------------------------------------|

from core.telegram import Telegram
Telegram_ = Telegram()


while True:
    last_message: dict[str, dict[str, Any]] = Telegram_.last_message()
    if last_message:
        for id_ in last_message.keys():
            data: dict[str, str] = last_message[id_]
            data["chat_id"] = str(id_)
            
            if Cache.TalkMode.open_account_branch.get(str(id_)):
                FIRST_EXEC.open_account_command(id_, data)
                continue
            
            FIRST_EXEC.first_commands(data)