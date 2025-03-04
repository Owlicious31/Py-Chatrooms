import pika

class MessageReceiver:

    def __init__(self) -> None:
        self.current_message = ""

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='messageQueue')
        self.channel.basic_consume(queue="messageQueue",on_message_callback=self.receive_message,auto_ack=True)
        self.channel.start_consuming()
        

    def receive_message(self,ch, method, properties, body) -> None:
        self.current_message = f"{body.decode("utf-8")}"
        self.stop_receiving_messages()
    

    def stop_receiving_messages(self) -> None:
        self.channel.stop_consuming()
