from .messages.receiver import MessageReceiver
from .messages.sender import MessageSender

class Session:

    def __init__(self) -> None:
        self.sender = MessageSender()
        self.receiver = MessageReceiver()

    def send_message(self,message: str) -> None:
        self.sender.send_message(message)
