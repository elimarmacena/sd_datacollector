import datetime
#import necessary to access postgresSQL database
import psycopg2
#used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
from common.environmentInfo  import *
#---------------------------------

def infoTop1():
	resultQuery = EnvironmentInfo.select().limit(1).get()
	hashResult = {  'temperature'   :   resultQuery.temperature,
					'moisture'      :   resultQuery.moisture,
					'pressure'      :   resultQuery.pressure,
					'send_data'     :   resultQuery.send_data,
					'latitude'      :   resultQuery.latitude,
					'longitude'     :   resultQuery.longitude,
					'owner'         :   resultQuery.owner}
	return hashResult

def getByTemperature(minTemp, maxTemp):
	resultQuery = EnvironmentInfo.select().where((EnvironmentInfo.temperature>=minTemp) & (EnvironmentInfo.temperature<=maxTemp))
	resultList = []
	for info in resultQuery:
		hashResult = {  'temperature'   :   info.temperature,
						'moisture'      :   info.moisture,
						'pressure'      :   info.pressure,
						'send_data'     :   info.send_data,
						'latitude'      :   info.latitude,
						'longitude'     :   info.longitude,
						'owner'         :   info.owner}
		resultList.append(hashResult)
	return resultList

def getByOwner(ownerName):
	resultQuery = EnvironmentInfo.select().where(EnvironmentInfo.owner == ownerName)
	resultList = []
	for info in resultQuery:
		hashResult = {  'temperature'   :   info.temperature,
						'moisture'      :   info.moisture,
						'pressure'      :   info.pressure,
						'send_data'     :   info.send_data,
						'latitude'      :   info.latitude,
						'longitude'     :   info.longitude,
						'owner'         :   info.owner}
		resultList.append(hashResult)
	return resultList

def getByDate(dateParameters):
	#converting into date type to use at query
	dayDate = datetime.date(int(dateParameters[2]),int(dateParameters[1]),int(dateParameters[0]) )
	dateFlow = datetime.date(int(dateParameters[2]),int(dateParameters[1]),int(dateParameters[0])+1 ) 
	resultQuery = EnvironmentInfo.select().where((EnvironmentInfo.send_data >= dayDate) & (EnvironmentInfo.send_data < dateFlow))
	resultList = []
	for info in resultQuery:
		hashResult = {  'temperature'   :   info.temperature,
						'moisture'      :   info.moisture,
						'pressure'      :   info.pressure,
						'send_data'     :   info.send_data,
						'latitude'      :   info.latitude,
						'longitude'     :   info.longitude,
						'owner'         :   info.owner}
		resultList.append(hashResult)
	return resultList

def getByDateInterval(dayMin,dayMax):
	dateMin = datetime.date(int(dayMin[2]),int(dayMin[1]),int(dayMin[0]))
	dateMax =  datetime.date(int(dayMax[2]),int(dayMax[1]),int(dayMax[0]))
	resultQuery = EnvironmentInfo.select().where( (EnvironmentInfo.send_data >= dateMin) & (EnvironmentInfo.send_data<=dateMax))
	resultList = []
	for info in resultQuery:
		hashResult = {  'temperature'   :   info.temperature,
						'moisture'      :   info.moisture,
						'pressure'      :   info.pressure,
						'send_data'     :   info.send_data,
						'latitude'      :   info.latitude,
						'longitude'     :   info.longitude,
						'owner'         :   info.owner}
		resultList.append(hashResult)
	return resultList