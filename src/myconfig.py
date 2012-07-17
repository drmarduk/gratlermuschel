'''
Created on Jun 25, 2012

@author: ente
'''
import datetime
class MyConfig(object):
	'''
	This class holds main config parameters
	'''

	_name = None
	_version = None
	_developers = None
	
	# time crap
	_start = None
	_lastget = None
	_refreshrate = None # in minutes
	
	#search stuff
	_hit_words = None
	
	# auth crap
	_consumer_key = None
	_consumer_secret = None
	_access_token = None
	_access_token_secret = None
	
	
	def __init__(self):
		'''
		Load default values
		'''
		self._name = "Gratlerbot"
		self._version = "0.1"
		self._developers = ["Marduk"]
		self._refreshrate = int(1)
		self._start = int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)) / datetime.timedelta(seconds = 1))
		self._lastget = self._start
		self._hit_words = [ "gratlermuschel" ]
		self._consumer_key = 'qJqihTltA8m6S0qNUkJig'
		self._consumer_secret = 'pwLm5xYT1LdOm8VKXk5bDnKG6aImfbeKrafmZTAu4'
		self._access_token = '618150249-qznfVx5gZwtRdndUAOUBeDlTCtH0UPrMk7uEROzS'
		self._access_token_secret = 'kJv05u67FzFR3PJoxD9SpqNyEJQoL13LISNj3jM'