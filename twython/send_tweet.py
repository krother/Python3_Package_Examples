
from twython import Twython

consumer_key = "INSERT_HASH"
consumer_secret = "INSERT_HASH"

access_token = "INSERT_HASH"
access_token_secret = "INSERT_HASH"

twitter = Twython(consumer_key, consumer_secret,
                  access_token, access_token_secret)

twitter.update_status(status="my first tweet from #python using twython")