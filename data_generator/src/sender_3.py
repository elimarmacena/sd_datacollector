import pika
import environment_generator as data_fac
import time
import datetime

print("THE SCRIPT WILL SEND INFORMATION EVERY 3 SECONDS TO THE MIDDLEWARE\n")
print("To exit press CTRL+C")

#ACCESS INRMATION
rabbit_host = 'localhost'
rabbit_userid = 'publisher_3'


credentials = pika.PlainCredentials(rabbit_userid,'123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=credentials))
properties = pika.BasicProperties(user_id=rabbit_userid);
channel = connection.channel()

count = 0
while(True):
    #data information
    temperature = data_fac.temperature_generator()
    moisture = data_fac.moisture_generator()
    pressure = data_fac.pressure_generator()
    location = [40.922123, -111.889029]
    currentDT = datetime.datetime.now()
    #-----------------
    information_pack = "%d;%d;%d;%f;%f;%s" % (temperature,moisture,pressure,location[0],location[1],currentDT.strftime('%Y-%m-%d %H:%M:%S'))
    channel.queue_declare(queue='hello',durable=True)
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=information_pack.encode(('utf-8')),
                      properties=properties)
    print("=>Information %i from %s Sent"%(count,rabbit_userid))
    count += 1
    time.sleep(3)

connection.close()