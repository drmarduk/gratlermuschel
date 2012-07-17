'''
Created on Jun 25, 2012

@author: ente
'''

class Tweet(object):
	'''
	Tweet class is managing the data of a tweet.
	json data is parsed
	
	and objectholder
	'''
	_rawjson = None
	_id = None
	_date = None
	_from_user = None
	_from_user_name = None
	_from_user_id = None
	_to_user = None
	_to_user_name = None
	_to_user_id = None
	_source = None
	_text = None
	_lang = None
	
	def __init__(self, json):
		'''
		Constructor
		'''
		#self._rawjson = str(json[0])
		#
		
		''' Parse data '''
		
		self._id = json['id_str']
		
		self._date = json['created_at']
		self._from_user = json['from_user']
		self._from_user_name = json['from_user_name']
		self._from_user_id = json['from_user_id_str']
		self._to_user = json['to_user']
		self._to_user_name = json['to_user_name']
		self._to_user_id = json['to_user_id_str']
		self._source = json['source']
		self._text = json['text']
		self._lang = json['iso_language_code']
		
		