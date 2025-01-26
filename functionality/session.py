import os
import json
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from util.exceptions import (
     SessionsInfoMissingException,
     MissingInfoException,
     NonExistentSessionException,
     InvalidMessageTypeException,
)

class Session:

    def __init__(self, index: int) -> None:

        self.index = index
        
        if not os.path.exists("../sessions_info.json"):
            raise SessionsInfoMissingException("Could not find sessions_info.json in the main directory")
        
        with open("../sessions_info.json") as file:
            try:
                self.session_info = json.load(file)[self.index]
            
            except IndexError:
                raise NonExistentSessionException(f"Was uanble to find a session at index: {index}")

            except json.decoder.JSONDecodeError:
                raise SessionsInfoMissingException("Could not load json file, likely empty.")
        
        try:    
            self.contact = self.session_info["contact"]
            self.messages = self.session_info["messages"]
        
        except KeyError:
            raise MissingInfoException("Was unable to construct session due to missing information in session info.")
        

    def update_messages(self,new_message: str) -> None:
        
        if not isinstance(new_message,str):
            raise InvalidMessageTypeException(f"Message: {new_message} is invalid, must be type 'str'")
        
        self.messages.append(new_message)
        self.session_info["messages"] = self.messages
        
        with open("../sessions_info.json") as file:
            try:
                sessions_data = json.load(file)

            except json.decoder.JSONDecodeError:
                raise SessionsInfoMissingException("Could not load json file, likely empty.")
            
        with open("../sessions_info.json","w") as file:
            sessions_data[self.index] = self.session_info
            json.dump(sessions_data,file,indent=4)


if __name__ == "__main__":
    session = Session(index=0)
    session.update_messages("updated")