# -*- coding: utf-8 -*-
import tweepy
import csv

# info
CONSUMER_KEY = 'IUd3NKZIbkLgBAiiYANhPdwfD'
CONSUMER_SECRET = 'kSZ0lMoZGIczEyzWkuWKxK5m0Sj1vrSXXgoTSpCBQt7DFXbnWA'
ACCESS_TOKEN = '280540266-ax7jhhAbHqlWwsJ6OuQBCTQlDxFrTaC3tccH0WuF'
ACCESS_SECRET = 'kTdX7uCTjdJkdezK3QLRqGamzhhbP29Y4FMPjPzlDvLkY'
COUNTRY = 'morocco'

# get authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# get tweets from country
place = api.geo_search(query=COUNTRY, granularity="country")
place_id = place[0].id

# print tweets and save to csv file
with open('tweets.csv', 'w', newline='', encoding='utf-8') as csvFile:
    tweetWriter = csv.writer(csvFile, delimiter=',')
    tweets = api.search(q='place:%s' % place_id, count=100, since='2018-11-5')
    count = 0
    for tweet in tweets:
        count += 1
        # tweet.id = unique id for tweet, text = text, place.name = where it was posted, created_at = UTC time
        tweetData = [tweet.id, tweet.user.name, tweet.created_at, tweet.text, tweet.place.name]
        tweetWriter.writerow(tweetData)

    print(count)