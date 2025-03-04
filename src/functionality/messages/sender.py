import pika

class MessageSender:

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="messageQueue")

    def send_message(self,message: str) -> None:

        self.channel.basic_publish(exchange='',
                      routing_key='messageQueue',
                      body=message)
        
        self.connection.close()
