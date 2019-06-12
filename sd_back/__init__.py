from sd_back.environment.get_informations import *
import os
from flask import Flask
from flask import json
from flask import request
from flask_cors import CORS
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	CORS(app)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# a simple page that says hello
	@app.route('/hello')
	def hello():
		return 'Hello, World!'

	# return top 1 data from BD
	@app.route('/top1')
	def top1():
		result = infoTop1()
		response = app.response_class(
			response=json.dumps(result),
			status=200,
			mimetype='application/json'
		)
		return response

	# return data based between two temperatures
	@app.route('/bytemperature')
	def byTemperature():
		try:
			minTemp = float(request.args.get('minTemp'))
			maxTemp = float(request.args.get('maxTemp'))
			if (maxTemp < minTemp):
				maxTemp = minTemp
			result = getByTemperature(minTemp, maxTemp)
			response = app.response_class(
				response=json.dumps(result),
				status=200,
				mimetype='application/json'
			)
			return response
		except Exception as err:
			print('Unable process the request.\n Erro type: %s' %(type(err)))
		return None

	# return data based in device owner
	@app.route('/byOwner')
	def byOwner():
		try:
			ownerName = request.args.get('owner')
			if(ownerName != None):
				result = getByOwner(ownerName)
				response = app.response_class(
					response=json.dumps(result),
					status=200,
					mimetype='application/json'
				)
				return response
		except Exception as err:
			print('Unable process the request.\n Erro type: %s' %(type(err)))
		return None

	# return data based in a specific day
	@app.route('/atDay')
	def atDay():
		try:
			dateString = request.args.get('date')
			if(dateString != None):
				# spling using in json information
				dateParametres = dateString.split('-')
				result = getByDate(dateParametres)
				response = app.response_class(
					response=json.dumps(result),
					status=200,
					mimetype='application/json'
				)
				return response
		except Exception as err:
			print('Unable process the request.\n Erro type: %s' %(type(err)))
		return None

	@app.route('/interValDate')
	def interValDate():
		try:
			dateStringMin = request.args.get('dateMin')
			dateStringMax = request.args.get('dateMax')
		
			if(dateStringMax != None and dateStringMin != None):
				dateMaxParameter = dateStringMax.split('-')
				dateMinParameter = dateStringMin.split('-')
				result = getByDateInterval(dateMinParameter, dateMaxParameter)
				response = app.response_class(
					response=json.dumps(result),
					status=200,
					mimetype='application/json'
				)
				return response
		except Exception as err:
			print('Unable process the request.\n Erro type: %s' %(type(err)))
		return app.response_class(
					status=400,
					mimetype='application/json'
				)

	@app.route('/getOwners')
	def getOwners():
		ownerList = []
		for owner in getOwnerList():
				ownerList.append(owner.owner)
		response = app.response_class(
			response = json.dumps(ownerList),
			status = 200,
			mimetype = 'application/json'
		)
		return response

	return app
