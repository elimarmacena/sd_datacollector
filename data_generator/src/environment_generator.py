import random
from peewee import *
from playhouse.postgres_ext import *


class EnvironmentInfo(Model):
    temperature = FloatField()
    moisture = FloatField()
    pressure = FloatField()
    send_data = DateTimeField()
    latitude = DoubleField()
    longitude = DoubleField()
    owner = CharField()
    class Meta:
        database =  PostgresqlDatabase('xxxxxx',
                                    user='xxxxxx',
                                    password='xxxxxxx',
                                    host='xxxxxxx', port=5432) 

def moisture_generator():
    return random.randint(0,100)

def pressure_generator():
    return random.randint(10,2000)

def temperature_generator():
    return random.randint(-30,60)