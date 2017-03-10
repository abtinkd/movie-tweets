consumer_key = "ddBG4wfBDhPmFAp0dDIyozVAr"
consumer_secret = "CgUiQ0vvXjNT4lnxJ6QbccKOhgXVR2QqvQ6qN3u8RunwgQk5wa"
access_token_key = "2478v0k6lg8kqs273200-ui6FN2wZGR3YuJxL1VI77YrqkdxK0"
access_token_secret = "UME9xsHbFUZEQYxDlp4HUVB5BtfbeVPNUCxvY2uO1K6jU"

from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'#oregonstate'})
print r.status_code

for item in r.get_iterator():
    print item['user']['screen_name'], item['text']
 