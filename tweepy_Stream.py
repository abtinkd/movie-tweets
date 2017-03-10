import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
from pymongo import MongoClient
import json


#Listener Class Override
class listener(StreamListener):

    def __init__(self, start_time, time_limit=60):

        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def on_data(self, data):

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

        while (time.time() - self.time) < self.limit:
            # try:
            #     client = MongoClient('localhost', 27017)
            #     db = client['twitter_db']
            #     collection = db['twitter_collection']
            #     tweet = json.loads(data)
                 
            #     collection.insert(tweet)
                 
            #     return True
            try:

                self.tweet_data.append(data)
                twt = json.loads(data)
                print twt['text']

                return True


            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass

        saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit()

    def on_error(self, status):

        print statuses
 



if __name__ == '__main__':

    consumer_key = "ddBG4p0dDIyozBDhPVAwfmFAr"
    consumer_secret = "CgUiQ06QbccVR2vvXjNT4lnxJQqvQ6qN3u8RunwgQk5wKOhgXa"
    access_token_key = "24780-ui6ZGR3Yu27320JxL1FNv0k6lg8kqs2wVI77YrqkdxK0"
    access_token_secret = "UME9xsHbFUVPNUCxvYEQYxDlp4Z5BtfbeHUVB2uO1K6jU"
     
    start_time = time.time() #grabs the system time
    keyword_list = ['lalaland'] #track list

    auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
    auth.set_access_token(access_token_key, access_token_secret)


    twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
    twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object



# api = tweepy.API(auth)


# def process_or_store(tweet):
#     print(json.dumps(tweet))

# # for status in tweepy.Cursor(api.home_timeline).items(10):
# #     # Process a single status
# #     print(status.text) 

# res = api.search(q="thesalesman")
# print help(api.search)
# for result in res:
#     print result.JSON
#     raw_input()


