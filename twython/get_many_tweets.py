"""
viele Tweets von Twitter sammeln.

Siehe README.TXT
"""

from twython import TwythonStreamer
from collections import Counter

consumer_key = "HIER EIGENEN CODE EINSETZEN"
consumer_secret = "HIER EIGENEN CODE EINSETZEN"

access_token = "HIER EIGENEN CODE EINSETZEN"
access_token_secret = "HIER EIGENEN CODE EINSETZEN"

tweets = []


class PyStreamer(TwythonStreamer):

    def on_success(self, data):
        if data.get('lang', '-') in ('en', 'de'):
            tweets.append(data)
            print('got tweet #{}'.format(len(tweets)))

        if len(tweets) == 100:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)


stream = PyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)

stream.statuses.filter(track='python')

# --------------- tweets analysieren -------------

# die Tweets sind ein riesiges Dictionary 
# voller 'Metadaten'
hashtags = Counter()
for tweet in tweets:
    for ht in tweet["entities"]["hashtags"]:
        hashtags.update([ht["text"]])
        # print(tweet["entities"]["hashtags"]["text"])
        # print(tweet['text'])

for ht in hashtags.most_common(10):
    print(ht, hashtags[ht])

