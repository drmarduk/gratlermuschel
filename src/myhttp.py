'''
Created on Jun 25, 2012

@author: ente
'''
import urllib.request, urllib.parse, urllib.request, urllib.error
import oauth
import string
import random
import datetime
import time
import hmac
import base64
import hashlib

class MyHttp(object):



	def __init__(self):
		'''
		Constructor
		'''
	def get(self, url):
		conn = urllib.request.urlopen(url, None)
		src = conn.read()
		return src
	
		
	def post(self, url, data):
		pass
	
	def oauth_req(self, url, key, secret, http_method = 'GET', post_body = None, http_headers = None):
		consumer = oauth.Consumer(key, secret)
		token = oauth.Token(key, secret)
		client = oauth.Client(consumer, token)
		
		resp, content = client.request(
									url, 
									http_method, 
									post_body, 
									http_headers, 
									0,
									None,
									True
									)
		return content
	
	
	def generateOAuthHeader(self, configinstance):
		if configinstance is None:
			return ''
		
		import myconfig
		cfg = myconfig.MyConfig()
		header = 'OAuth '
		header += 'oauth_consumer_key="' + cfg._consumer_key + '", '
		header += 'oauth_nonce="' + ''.join(random.choice(string.ascii_uppercase) for x in range(6)) + '", '
		header += 'oauth_signature="' + urllib.parse.quote("asf") + '", '
		header += 'oauth_signature_method="HMAC-SHA1", '
		header += 'oauth_timestamp="' + str(int((time - datetime.datetime(1970, 1, 1)) / datetime.timedelta(seconds = 1))) + '", '
		header += 'oauth_token="' + cfg._access_token + '", '
		header += 'oauth_version="1.0"'
		
		return header

	

class oauthhttp():
	headers = None
	post = None
	host = None
	url = None
	method = None
	
	oauthHeader = None
	
	oauth_consumer_key = None
	oauth_consumer_secret = None
	oauth_token = None
	oauth_token_secret = None
	oauth_nonce = None
	oauth_signature = None
	oauth_timestamp = None
	
	
	def __init__(self):
		self.headers = {'Accept' : '*/*',
				'Connection' : 'close',
				'User-Agent' : 'olololNerdyPerdyTrolliBot',
				'Content-Type' : 'application/x-www-form-urlencoded',
				'Host' : 'api.twitter.com',
				'Content-Length' : '0',
				'Authorization' : ''}
		
		self.oauthHeader = 'OAuth oauth_consumer_key="{0}", ' + \
		'oauth_nonce="{1}", ' + \
		'oauth_signature="{2}", ' + \
		'oauth_signature_method="HMAC-SHA1", ' + \
		'oauth_timestamp="{3}", ' + \
		'oauth_token="{4}", ' + \
		'oauth_version="1.0"'
		
		self.oauth_nonce = self.generateNonce()
		self.oauth_timestamp = self.generateTimestamp()
		
		
	def request(self, url, method, data):
		params = {'oauth_consumer_key': self.oauth_consumer_key,
		'oauth_nonce': self.oauth_nonce,
		'oauth_signature_method':'HMAC-SHA1',
		'oauth_timestamp': self.oauth_timestamp,
		'oauth_token': self.oauth_token,
		'oauth_version':'1.0'}
		postdata = ''
		# add default data crap
		for key in data.keys():
			params[key] = data[key]
			postdata += key + '=' + self.encode(data[key]) + '&'
			
		postdata = postdata[:-1]
						
		self.oauthHeader = self.oauthHeader.format(self.oauth_consumer_key, 
												self.oauth_nonce,
												self.encode(self.generateSignature(url, method, params, self.oauth_consumer_secret, self.oauth_token_secret)), 
												self.oauth_timestamp,
												self.oauth_token)
		
		req = urllib.request.Request(url, postdata.encode('ascii'), {'Authorization' : self.oauthHeader})
		try:
			f = urllib.request.urlopen(req)
			src = f.read()
		except urllib.error.HTTPError as e:
			print(e.code)
			print(e)
		else:
			
			return src
	
	def setKeys(self, oauth_consumer_key, oauth_token):
		self.oauth_consumer_key = oauth_consumer_key
		self.oauth_token = oauth_token
	
	def setSecret(self, consumer_secret, token_secret):
		self.oauth_consumer_secret = consumer_secret
		self.oauth_token_secret = token_secret
		
	def generateNonce(self):
		return ''.join(random.choice(string.ascii_letters) for x in range(32))
		pass
	
	def generateTimestamp(self):
		tmp = int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)) / datetime.timedelta(seconds = 1))
		return tmp.__str__()
	
	def generateSignature(self, baseurl, method, params, consumer_secret, token_secret):
		dst = ''
		for key in sorted(params.keys()):
			dst += '&' + key + '=' + self.encode(params[key])
		dst = dst[1:]
		
		dst = method + '&' + urllib.parse.quote_plus(baseurl) + '&' + self.encode(dst)
		
		signkey = self.encode(consumer_secret) + '&' + self.encode(token_secret)
		hashs = hmac.new(signkey.encode('ascii'), dst.encode('ascii'), hashlib.sha1)
		result = base64.encodestring(hashs.digest())
		return result.decode('ascii')
		
	def encode(self, msg):
		return urllib.parse.quote(msg)
	
		
		