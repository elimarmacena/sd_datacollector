import random

def moisture_generator():
    return random.randint(0,100)

def pressure_generator():
    return random.randint(10,2000)

def temperature_generator():
    return random.randint(-30,60)