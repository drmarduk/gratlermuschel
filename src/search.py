'''
Created on Jun 25, 2012

@author: ente
'''
import jsonparser
import twitter
import tweet
import urllib.parse
import datetime

class Search(object):
	'''
	classdocs
	'''
	_query = None
	_id = None
	_refresh_url = None
	_results = None
	_raw_json = None
	_tweets = None

	def __init__(self, query):
		self._query = urllib.parse.quote(query)
		self._tweets = list()
		self._init = True
		
	def performSearch(self):
		_twitter = twitter.Twitter()
		if self._refresh_url is not None:
			self._raw_json = _twitter.search(self._query, self._refresh_url)
		else:
			self._raw_json = _twitter.search(self._query)
		self.parse()
		
	def parseID(self):
		parser = jsonparser.JSONParser(self._raw_json)
		self._id = parser.getValue("max_id")
		
	
	def parseRefreshURL(self):
		parser = jsonparser.JSONParser(self._raw_json)
		self._refresh_url = parser.getValue("refresh_url")
		
	def parseResults(self):
		parser = jsonparser.JSONParser(self._raw_json)
		self._results = parser.getValue("results")
		# parse tweets
		for entry in self._results:
			tmp = tweet.Tweet(entry)
			self._tweets.append(tmp)
			
		
	def parse(self):
		self.parseID()
		self.parseRefreshURL()
		self.parseResults()
		
	def reset(self):
		self._tweets = list()
			