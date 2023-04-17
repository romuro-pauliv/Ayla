# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                  app.log.terminal.database.open_account.connect.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from colorama import Fore, Style
# |--------------------------------------------------------------------------------------------------------------------|

class OpenAccountLog(object):
    @staticmethod
    def open_database(chat_id: str, db: str) -> None:
        method_: str = f"[{Fore.GREEN}POST{Style.RESET_ALL}]"
        db_info: str = f"{Fore.MAGENTA}||DB||"
        chat_id_terminal: str = f"{Style.RESET_ALL}@{chat_id}"
        func: str = f"{Fore.GREEN}OPEN DATABASE{Style.RESET_ALL}"
        
        print(f"{method_} {db_info} {chat_id_terminal} [{Fore.GREEN}{db}{Style.RESET_ALL}] -> {func}")
    
    @staticmethod
    def open_wallet_list(chat_id: str, db: str) -> None:
        method_: str = f"[{Fore.GREEN}POST{Style.RESET_ALL}]"
        db_info: str = f"{Fore.MAGENTA}||DB||"
        chat_id_terminal: str = f"{Style.RESET_ALL}@{chat_id}"
        
        db_terminal: str = f"[{Fore.GREEN}{db}{Style.RESET_ALL}]"
        coll_terminal: str = f"[{Fore.CYAN}/WALLETS{Style.RESET_ALL}]"
        func: str = f"{Fore.GREEN}OPEN WALLET LIST{Style.RESET_ALL}"
        
        print(f"{method_} {db_info} {chat_id_terminal} {db_terminal} {coll_terminal} -> {func}")
    
    @staticmethod
    def open_wallet_collection(chat_id: str, db: str, coll: str) -> None:
        method_: str = f"[{Fore.GREEN}POST{Style.RESET_ALL}]"
        db_info: str = f"{Fore.MAGENTA}||DB||"
        chat_id_terminal: str = f"{Style.RESET_ALL}@{chat_id}"
        
        db_terminal: str = f"[{Fore.GREEN}{db}{Style.RESET_ALL}]"
        coll_terminal: str = f"[{Fore.CYAN}{coll}{Style.RESET_ALL}]"
        func: str = f"{Fore.GREEN}OPEN WALLET COLL{Style.RESET_ALL}"
        
        print(f"{method_} {db_info} {chat_id_terminal} {db_terminal} {coll_terminal} -> {func}")