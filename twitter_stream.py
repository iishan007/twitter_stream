from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import tweepy
import csv
import datetime

#consumer key, consumer secret, access token, access secret.
ckey = ''
csecret = '' 
atoken = '' 
asecret = ''

class CustomStreamListener(tweepy.StreamListener):

	#Fetch Date & Time of Streaming.
	now = datetime.datetime.now()
	now_str = now.strftime("%Y-%m-%d")

	#Here, we save the file in csv format with current date & time of streaming.
	global writer
	file_name = 'tweets_data-{}.csv'.format(now_str)
	writer = csv.writer(open(file_name,'w+'))
	writer.writerow(('Author', 'Date', 'Text'))

	#Uncomment this section, if you want to save file into txt file.
	#def on_data(self, data):
		#print data
		#with open('fetched_tweets.txt','w') as tf:
			#tf.write(data)
		#return True
	
	def on_status(self, status):
		print status.author.screen_name, status.created_at, status.text.encode('utf-8')
		item_list = [status.author.screen_name, status.created_at, status.text.encode('utf-8')]
		writer.writerow(item_list)	
        
	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream 

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
streamingAPI.filter(track=['happy'])