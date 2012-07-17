'''
Created on Jun 25, 2012

@author: ente
'''
import myconfig
import datetime
import time
import search
import myhttp
import ai
import twitter


def strtime(fmt = True):
	'''
	@param format boolean defines wether to return unix timestamp or formatted string
	'''
	time = datetime.datetime.now()
	if fmt == True:
		return time
	else:
		return int((time - datetime.datetime(1970, 1, 1)) / datetime.timedelta(seconds = 1))
	
	
def main():
	# Init stuff
	cfg = myconfig.MyConfig()
	
	# le loop
	_search = search.Search("gratlermuschel") #multi query search support, siehe myconfig
	_twitter = twitter.Twitter()
	
	_search.performSearch()
	_search.reset()
	
	while True: # should be changed to user interrupt/cat reply or nuclear attack
		time.sleep(1)
		
		if (int(strtime(False)) - int(cfg._lastget)) > (cfg._refreshrate * 60):
			# do updatessss
			cfg._lastget = int(strtime(False))
			print('Perform Search - {0}'.format(strtime(True)))
			
			_search.performSearch()
			print(str(len(_search._tweets)) + ' neue Tweets:')
			
			if len(_search._tweets) > 0:
				for i in _search._tweets:
					# antworten an i.from_user
					print('{2} - {0}: {1}'.format(i._from_user, i._text.encode('utf-8'), i._date))
					#antworten
					_ai = ai.AI()
					if i._from_user is not None:
						_ai.addFromUser(i._from_user)
					if i._to_user is not None:
						_ai.addToUser(i._to_user)
						
					answer = _ai.getAnswer(i._text)
					_twitter.tweet(answer)
					print('--->geantwortet')
					
						
			_search.reset()

				

if __name__ == '__main__':
	main()
	#test()
	
	
	