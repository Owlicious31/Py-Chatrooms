import os
import threading
import time
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from functionality.messages.receiver import MessageReceiver
from functionality.messages.sender import MessageSender

class Session:

    def __init__(self) -> None:
        self.sender = MessageSender()
        self.receiver = MessageReceiver()

        self.all_messages = self.receiver.messages
        threading.Thread(target=self.process_and_return_message).start()


    def process_and_return_message(self,message: str) -> list[str]:
        self.sender.send_message(message)
        return self.receiver.messages
