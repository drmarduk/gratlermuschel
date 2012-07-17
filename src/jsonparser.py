'''
Created on Jun 26, 2012

@author: ente
'''
import json

class JSONParser(object):
	'''
	Parsing json using key search and return some json or values
	'''
	_raw = None

	def __init__(self, rawjson):
		'''
		Constructor
		'''
		self._raw = rawjson.replace('\'', '"').replace('None', 'null')
		
	def getValue(self, key):
		d = json.loads(self._raw)
		return d[key]
		