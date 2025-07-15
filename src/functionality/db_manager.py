import sys
from tinydb import TinyDB, Query

ENVIRONMENT = "PROD"

class DatabaseManager:

    def __init__(self) -> None:
        if ENVIRONMENT == "PROD":
            self.db = TinyDB("./sessions_info.json")
        
        elif __name__ == "__main__":
            self.db = TinyDB("../../test_info.json")
        
        else:
            self.db = TinyDB("./test_info.json")
            
        self.Chat = Query()

        for session in self.db:
            if len(session["messages"]) >= 250:
                self.update_message_history(session["name"],session["messages"][125:])

        self.available_sessions = self.db.all()

    
    def get_message_history(self,chat_name: str) -> list[str]:
        session_info = self.db.search(self.Chat.name == chat_name)  
        return session_info[0]["messages"]
    

    def update_message_history(self,chat_name: str,new_messages: list[str]) -> None:
        self.db.update({"messages":new_messages},self.Chat.name == chat_name)

    
    def create_new_session(self,chat_name: str) -> None:
        self.db.insert({"name":chat_name,"messages":[]})
    
