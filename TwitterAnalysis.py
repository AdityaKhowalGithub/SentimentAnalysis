import GetOldTweets3 as got
#import datetime 
import datetime as dt
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()

current = str(dt.datetime.now().date())
input = input("Enter the keyword/hashtag to search about: ")

def get_tweets(input):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                           .setSince("2015-05-01")\
                                           .setUntil("2015-09-30")\
                                           .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.text)

get_tweets(input)