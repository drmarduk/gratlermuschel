'''
Created on Jul 2, 2012

@author: ente
'''
import random
import re

class AI(object):
	'''
	artificial kann man das zwar net nennen, soll aber auf gewisse Schlagworte in der Nachricht eingehen.
	Ist eine Beleidigung/Smiley/Hashtag/Frage in der Nachricht, soll darauf reagiert werden.
	
	Im Moment ist das alles noch mehr so random
	
	'''
	base = None
	from_user = None
	to_user = None
	hashtags = None
	
	# answers Smileys
	aSmiley = [' Sorry, dass sind mir zu viele Smileys', 
			' :)', 
			' (╯°□°）╯︵ ┻━┻', 
			' :>',
			' >:|',
			' -.-',
			' -.-"',
			' \o/',
			' *FU*',
			' :D',
			' :*',
			' >.>',
			' >.<',
			' o.O',
			' Ich verstehe dieses Smiley nicht']
	
	#answers oder
	aOder = [' {0} und {1}',
			' {0} oder {1} #Gegentweet',
			' Ich hab sowohl von {0} als auch von {1} nur Schlechtes gehoert.', 
			' beides scheisse.', 
			]
	
	aMama = [' Deine Mama.', 
			' Koennte ich von deiner Mama auch sagen.', 
			' #deineMamaTweet', 
			' Sag deiner Mama, die soll mein Klo putzen.']
	
	aInsult = [' Penner',
			' Arschloch',
			' Depp',
			' Arsch',
			' Fotze',
			]
	
	def __init__(self):
		pass
		
	def addFromUser(self, user):
		if user is not None:
			self.from_user = user.lower()
			
	def addToUser(self, user):
		if user is not None:
			self.to_user = user
	
	def addHashtag(self, tag):
		for i in tag:
			self.hashtags.append(i)
		
	
	def getAnswer(self, message):
		'''
		Wie gesagt, der Entscheidungsweg nicht so ganz trivial, momentan ist die Prioritaet:
			- Mention von @gratlermuschel an @gratlermuschel (Waere moeglich, wenn x Stunden kein Aktion kam, dass er sich selbst mentioned (wobei auf rekursion fuck zu achten ist))
			- [..]
			- "blau oder rot" Fragen
			- Smileycount > 2 mit nem Smiley antworten = siehe dysthymija wahn
			- ...
		'''
		try:
			if 'gratlermuschel' in self.from_user:
				return '@' + self.from_user + ' dir antworte ich natuerlich auch, Depp'
			elif ' oder ' in message:
				answer = '@' + self.from_user + ' ' + self.oder(message)
			elif self.smileycount(message) > 2:
				answer = self.aSmiley[self.rand(len(self.aSmiley))]
			else:
				answer = '@' + self.from_user + ' keine Ahnung was du von mir willst.'
			return answer
		except:
			if self.from_user is not None:
				return '@' + self.from_user + ' ich mag dich nicht.'
			else:
				return 'WTF was war das denn?'
			
	
	def oder(self, text):
		'''
		Ideal waere eine Antwort "@gratlermuschel rot oder blau?
		Und eins der Entscheidungen geht zurueck		
		'''
		text = text.replace('#gratlermuschel ', '').replace('@gratlermuschel ', '').replace('?', '')
		ar = text.split(' oder ')
		return ar[self.rand(len(ar))]
	
		
	def smileycount(self, text):
		'''
		Smileycount in der Message ermitteln 
		'''
		p = re.compile('[ÒÓÔòóôoO0xXZz~_<>:;-]{1}[.v_]{0,5}[ÒÓÔòóôoO0xXZz~<>DpP(/)-]{1}["#]{0,1}')
		count = len(p.findall(text))
		return count
		
	def isInsult(self, text):
		p = re.compile('((p|P)enner|(d|D)epp|(a|A)rsch|(f|F)otze|doof|bl(.|oe)d|(h|H)ure)')
		count = len(p.findall(text))
		return count
	
	def isQuestion(self, text):
		return text.endswith('?')
		pass
	
	def rest(self):
		# temp fuer irc
		if 'evilpie' in self.from_user:
			answer = '@' + self.from_user + ' doedoedoe'
		if 'dysthymija' in self.from_user:
			answer = '@' + self.from_user + ' du und deine Smileys wieder.'
		if 's00da' in self.from_user:
			answer = '@' + self.from_user + ' geh lernen!'
		if 'karottenkostuem' in self.from_user:
			answer = '@' + self.from_user + ' do you need an antivirustool?'
		if 'dukeofnuts' in self.from_user:
			answer = '@' + self.from_user + ' stell dich in den Regen, dann waechst du.'
		if 'aaimless' in self.from_user:
			answer = '@' + self.from_user + ' THIS IS RICCARDO, ME WANTS IPADS, NOW.'
		if 'maRv1' in self.from_user:
			answer = '@' + self.from_user + ' ich blute, kannst du mir ein Pflaster geben?'	
		if 'txt_input' in self.from_user:
			answer = '@' + self.from_user + ' dir antworte ich nicht, anderen vielleicht'
		return answer
	
	def rand(self, _max = 2):
		if _max is not None:
			r = random.Random()
			return r.randint(0, _max - 1)
		else:
			return 0
	
	
		
