from tinydb import TinyDB, Query

class DatabaseManager:

    def __init__(self) -> None:
        self.db = TinyDB("../../sessions_info.json")
        self.Chat = Query()

        self.available_session = self.db.all()

        for session in self.db:
            if len(session["messages"]) > 1000:
                self.update_message_history(session["name"],session["messages"][:500])

    
    def get_message_history(self,chat_name: str) -> list[str]:
        session_info = self.db.search(self.Chat.name == chat_name)  
        return session_info[0]["messages"]
    

    def update_message_history(self,chat_name: str,new_messages: list[str]) -> None:
        self.db.update({"messages":new_messages},self.Chat.name == chat_name)

    
    def create_new_session(self,chat_name: str) -> None:
        self.db.insert({"name":chat_name,"messages":[]})



if __name__ == "__main__":
    dm = DatabaseManager()
    dm.create_new_session("chat2")
    