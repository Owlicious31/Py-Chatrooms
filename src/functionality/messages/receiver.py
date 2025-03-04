import threading
import pika

class MessageReceiver:

    def __init__(self) -> None:
        self.messages = []

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        
        self.channel.exchange_declare(exchange='chatExchange', exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True) 
        
        queue_name = result.method.queue
        self.channel.queue_bind(exchange='chatExchange', queue=queue_name)
        
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.receive_message, auto_ack=False)
        
        threading.Thread(target=self.listen_for_messages, daemon=True).start()


    def listen_for_messages(self) -> None:
        try:
            self.channel.start_consuming()
        except:
            self.stop_receiving_messages()
        

    def receive_message(self,ch, method, properties, body) -> None:
        self.messages.append(f"{body.decode("utf-8")}")
        ch.basic_ack(delivery_tag=method.delivery_tag)  


    def stop_receiving_messages(self) -> None:
        self.channel.stop_consuming()
        self.connection.close()
