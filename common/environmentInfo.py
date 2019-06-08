from peewee import *

class EnvironmentInfo(Model):
    temperature = FloatField()
    moisture = FloatField()
    pressure = FloatField()
    send_data = DateTimeField()
    latitude = DoubleField()
    longitude = DoubleField()
    owner = CharField()
    class Meta:
        database =  PostgresqlDatabase('kqfjcilw',
                                    user='kqfjcilw',
                                    password='fmyBJ-WKIjxE7SdlZXniE1BV-_aHFlkn',
                                    host='motty.db.elephantsql.com', port=5432) 
