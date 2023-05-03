# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app.connections.send_log.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.paths import MicrosservicesAPI

from typing import AnyStr
import requests
# |--------------------------------------------------------------------------------------------------------------------|


class SendToLog(object):
    def __init__(self) -> None:
        self.host: str = MicrosservicesAPI.MS_ROUTES["logs"]["HOST"]
        self.port: str = MicrosservicesAPI.MS_ROUTES["logs"]["PORT"]
        self.dir: str = MicrosservicesAPI.MS_ROUTES["logs"]["DIR"]
        
    def report(self, REPORT: str, LOG_LEVEL: str, chat_id: str) -> None:
        """
        Send to MS LOG a report
        Args:
            REPORT (str): Log information
            LOG_LEVEL (str): Log level ["debug", "info", "warning", "error", "critical"]
            chat_id (str): chat_id generator of the log report
        """
        debug_endpoint: str = MicrosservicesAPI.MS_ROUTES["logs"]["ENDPOINTS"][LOG_LEVEL]
        send_json: dict[str] = {
            "report": REPORT,
            "extra": {"microservice": "GATEWAY", "clientip": "LOCAL", "chat_id": chat_id}
        }
        try:
            requests.post(f"{self.host}:{self.port}{self.dir}{debug_endpoint}", json=send_json)
        except requests.exceptions.ConnectionError:
                pass