import time
import sys
import json
from TwitterSearch import *

OAuth = TwitterSearch(
      consumer_key = 'EFBFU5OyPJ8eogw98nubFYqrv',
      consumer_secret = 'LH8NdCZcGi5fgWe9tWrbTdbnB5EdFs05XV03fG1x8guleeu0S5',
      access_token = '2828646955-lGyZgUyrBoeoWguK9BzumA5tYKHmbchm9IOIcXB',
      access_token_secret = '15OrYXdvW1BcaQZYHSqFfKcn37uDuSYwlOig5T7VwgHWr'
    )

for ii in range(1, 100):
  try:
    congress_tweets = TwitterSearchOrder()
    congress_tweets.setKeywords(['#ca17', '#CA17'])
    congress_tweets.setLanguage('en')
    congress_tweets.setCount(100)
    congress_tweets.setIncludeEntities(False)
    if ii > 1:
      congress_tweets.setSinceID(since_id)
    json_list = list() 
    for tweet in OAuth.searchTweetsIterable(congress_tweets):
      json_list.append(tweet)
      json_list.append(tweet)
    #probably not the best way to do it. Once the rate limit comes back up. Sort the list by ids
    #and then pick up the most recent id. for the since id
    since_id = int(json_list[-1]['id'])
    with open("tweets_data/test/%s.json" %("hashtag_CA17_" + str(ii)), "w") as output:
      json.dump(json_list, output)
  except TwitterSearchException as e:
    print e
    print "Something went wrong"
  time.sleep(2)
