import sys
import jsonpickle
import os
from pymongo import MongoClient
import json
import tweepy
import time


consumer_key = API_KEY = "ddBG4wfmFIyozBDhPVAAp0dDr"
consumer_secret = API_SECRET = "ChgXVR2vvXjNTgUiQ06QbccKO4lnxJQqvQ6qN3u8RunwgQk5wa"
access_token_key = "24780k6lg8kqs2wZG273200-ui6FNvR3YuJxL1VI77YrqkdxK0"
access_token_secret = "UME9xsHbFlp4HUVB2uO1K6jUUZ5BtfbeVPNUCxvYEQYxD"
 
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #OAuth object

client = MongoClient('localhost', 27017)
db = client['CS540_db']
collection = db['twitter_collection']

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)
 
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
 
# Continue with rest of code

movie_list = []
with open('movies_imdb.txt') as f:
    content = f.readlines()
    movie_list = ['\"'+x.strip()+'\"' for x in content]

maxTweets = 5000 # Some arbitrary large number
tweetsPerQry = 100 # this is the max the API permits
fName = 'tweets.json' # We'll store the tweets in a text file.
sinceId = None
# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
for i in xrange(len(movie_list)):
    max_id = -1L
    searchQuery = movie_list[i]
    tweetCount = 0
    print("Downloading max {0} tweets for Movie: {1}".format(maxTweets, searchQuery))
    with open(fName, 'a') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, lang="en", count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery, lang="en", count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, lang="en", count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery, lang="en", count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break

                for tweet in new_tweets:                    
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                    #                    
                    # tw = jsonpickle.encode(tweet._json, unpicklable=False)
                    collection.insert(tweet._json) 
                    #
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))