from messages.receiver import MessageReceiver
from messages.sender import MessageSender

class Session:

    def __init__(self) -> None:
        self.sender = MessageSender()
        self.receiver = MessageReceiver()

        self.all_messages = self.receiver.messages


    def process_and_return_message(self,message: str) -> list[str]:
        self.sender.send_message(message)
        return self.receiver.messages
    
#TODO - replace returning messages with listening for messages and update gui whenever new message is sent
#TODO - add listen for messages method
