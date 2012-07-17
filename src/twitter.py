'''
Created on Jun 25, 2012

@author: ente
'''
import myhttp
import myconfig


class Twitter(object):
	'''
	Main twitter class for managing search, post
	'''
	_api = None
	_searchapi = None
	_cfg = None
	'''
		q				Query
		page			page to show, max 1500 = page * rpp
		rpp				tweets per page, max 100
		result_type 	recent, mixed, popular
		until			tweets written before YYY-MM-DD
		
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self._api = "https://api.twitter.com/"
		self._searchapi = "http://search.twitter.com/search.json"
		self._cfg = myconfig.MyConfig()
		
		
	def search(self, query, refresh_url = None):
		'''
		Main search function, mainly used for hashtagsearch
		@param string query main query string
		'''
		if refresh_url == None:
			param = '?q=' + query + "&result_type=recent&rpp=100&page=1"
		else:
			param = refresh_url
		url = self._searchapi + param
		net = myhttp.MyHttp()
		jsonresponse = net.get(url)
		return bytes.decode(jsonresponse)
		
	def mention(self, message, user):
		'''
		send a mention to your timline with user
		'''
		print("Class: {0} - Method: {1}".format(self.__class__, self.mention.__name__))
		
	def tweet(self, message):
		'''
		send a tweet with message
		'''
		net = myhttp.oauthhttp()
		params = {'status': message}
		net.setKeys(self._cfg._consumer_key, self._cfg._access_token)
		net.setSecret(self._cfg._consumer_secret, self._cfg._access_token_secret)
		src = net.request('https://api.twitter.com/1/statuses/update.json', 'POST', params)
		
	