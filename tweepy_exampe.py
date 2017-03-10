from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="DIyozBDhPVArddBG4wfmFAp0d"
consumer_secret="XjNT4lnxJQqvQ6qN3u8RunwgQk5waCgUiQ06QbccKOhgXVR2vv"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="lg8kqs2wZGR3YuJxL1VI77YrqkdxK02478002732-ui6FNv0k6"
access_token_secret="UME9NUCxvYEQYxDlp4HUVB2uO1K6jUxsHbFUZ5BtfbeVP"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])