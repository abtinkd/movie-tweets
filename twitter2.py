import twitter

consumer_key = "dd4wfmFAp0dDIyBGozBDhPVAr"
consumer_secret = "CgUiQ06QbccXjNT4lnxJQqKOhgXVR2vvvQ6qN3u8RunwgQk5wa"
access_token_key = "24782lg8kqs2wZGR73200-ui6FNv0k63YuJxL1VI77YrqkdxK0"
access_token_secret = "UME9xsHbFUZ5BtEQYxDlp4HUVfbeVPNUCxvYB2uO1K6jU"

aapi = twitter.api(consumer_key=[consumer_key],
                  consumer_secret=[consumer_secret],
                  access_token_key=[access_token_key],
                  access_token_secret=[access_token_secret])

print(aapi.VerifyCredentials())