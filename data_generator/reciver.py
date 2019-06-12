import pika
import environment_generator as eg
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)


def callback(ch, method, properties, body):
    information_pack = body.decode('utf-8').split(';')
    try:
        environment_information = eg.EnvironmentInfo(temperature=float(information_pack[0]),
                                    moisture =float(information_pack[1]),
                                    pressure= float(information_pack[2]),
                                    send_data=datetime.datetime.strptime(information_pack[5], '%Y-%m-%d %H:%M:%S'),
                                    latitude= float(information_pack[3]),
                                    longitude= float(information_pack[4]),
                                    owner= properties.user_id)
        environment_information.save()
    except Exception as err:
        print('Unable process the information recieved.\n Erro type:%s \n' %(type(err)))
    print(" [x] Received %r  from %s" % (body.decode('utf-8'),properties.user_id))


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()