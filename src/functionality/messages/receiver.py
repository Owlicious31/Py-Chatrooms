import threading
import pika

class MessageReceiver:

    def __init__(self) -> None:
        self.messages: list[str] = []

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        
        self.channel.exchange_declare(exchange='chatExchange', exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True) 
        
        queue_name = result.method.queue
        self.channel.queue_bind(exchange='chatExchange', queue=queue_name)
        
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.receive_message, auto_ack=False)
        
        threading.Thread(target=self.listen_for_messages, daemon=True).start()


    def listen_for_messages(self) -> None:
        """
        Listen for messages being sent to the exchange and execute protocol for receiving messages.
        Any exceptions will cause the channel to stop listening for messages and close the connection.
        :return: None
        """
        try:
            self.channel.start_consuming()
        except:
            self.stop_receiving_messages()
        

    def receive_message(self,ch, method, properties, body) -> None:
        """
        Receive messages sent to the queue and append them to the instance's list of messages.
        :return: None
        """
        self.messages.append(f"{body.decode("utf-8")}")
        ch.basic_ack(delivery_tag=method.delivery_tag)  


    def stop_receiving_messages(self) -> None:
        """
        Stop listening for messages and close the active connection.
        """
        self.channel.stop_consuming()
        self.connection.close()
