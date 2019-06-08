import random

#used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
from common.environmentInfo  import *
#---------------------------------

def moisture_generator():
	return random.randint(0,100)

def pressure_generator():
	return random.randint(10,2000)

def temperature_generator():
	return random.randint(-30,60)

data = EnvironmentInfo.select().where(EnvironmentInfo.owner=='publisher_2').limit(1).get()
print(data.pressure)
print(data.owner)
