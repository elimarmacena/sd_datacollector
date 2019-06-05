import pika

rabbit_host = 'localhost'

rabbit_userid = 'publisher_1'


credentials = pika.PlainCredentials(rabbit_userid,'123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=credentials))
properties = pika.BasicProperties(user_id=rabbit_userid);
channel = connection.channel()

count = 0
while(count < 1000):
    channel.queue_declare(queue='hello',durable=True)
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='SEND DATA!'+str(count),
                      properties=properties)
    print(" [x] Sent 'Hello World!'"+str(count))
    count += 1

connection.close()