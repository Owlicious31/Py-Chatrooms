

class SessionManager:

    def __init__(self) -> None:
        self.all_sessions: list[dict] = [{"name":f"test{i}"} for i in range(6)]
    
# TODO - Make session manager class that takes the initialized user's sessions info and saves
# it in a var "all_sessions" and has methods for creating and adding new sessions to the db and 
# adding existing sessions from other users to the user's sessions info and appending it to all_sessions