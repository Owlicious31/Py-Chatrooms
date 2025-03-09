import pika

class MessageSender:

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='chatExchange', exchange_type='fanout')
        self.channel.confirm_delivery()


    def send_message(self,message: str) -> None:
        """
        Send a message to a central chat exchange. Messages are subsequently distributed to receiving queues.
        :param message: The message being sent
        :return: None
        """
        self.channel.basic_publish(exchange='chatExchange',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode = pika.DeliveryMode.Persistent)
                      )
