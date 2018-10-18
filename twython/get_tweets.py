"""
aktuelle Tweets von Twitter suchen.

Siehe README.TXT
"""

from twython import Twython

consumer_key = "HIER EIGENEN CODE EINSETZEN"
consumer_secret = "HIER EIGENEN CODE EINSETZEN"

twitter = Twython(consumer_key, consumer_secret)

for status in twitter.search(q='python berlin')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print(user)
    print(text)
    print(status['created_at'])
    print()
