import csv
import pandas
import tweepy
from textblob import TextBlob

consumer_key = #
c_key_sec = #

access_token = #
a_token_sec = #

auth = tweepy.OAuthHandler(consumer_key,c_key_sec)
auth.set_access_token(access_token,a_token_sec)

api = tweepy.API(auth)
search_string = str(input("Enter search string:"))

pub_tweets =api.search(search_string)
tweet_l = []
tweet_analysis = []

df = pd.read_csv('tweets.csv',delimiter = ' ')
print(df.head())

with open('tweets.csv', 'w') as csvfile1:
	writetweet = csv.writer(csvfile1, delimiter = ' ')
	for tweet in  pub_tweets:
		writetweet.writerow([tweet.text])
		analysis = TextBlob(tweet.text)
		writetweet.writerow([analysis.sentiment])

print("Ten tweets written to csv file")
