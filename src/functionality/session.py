from .messages.receiver import MessageReceiver
from .messages.sender import MessageSender

class Session:

    def __init__(self) -> None:
        self.sender = MessageSender()
        self.receiver = MessageReceiver()

    def send_message(self,message: str) -> None:
        """
        Call the instance's MessageSender's send_message method on the given message.
        :param message: The message being sent.
        :return: None
        """
        self.sender.send_message(message)
