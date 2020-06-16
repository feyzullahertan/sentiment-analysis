import tweepy
import pyodbc


my_consumer_key = "XXXXXXX"
my_consumer_secret = "XXXXXXX"
my_access_token = "XXXXXXX"
my_access_token_secret = "XXXXXXX"


auth = tweepy.OAuthHandler(my_consumer_key, my_consumer_secret)
auth.set_access_token(my_access_token, my_access_token_secret)

realdb=pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=.;'
        r'DATABASE=Coronavirus;'
        r'Connection Timeout=0;'
        r'Trusted_Connection=yes;'
        )
my_cursor=realdb.cursor()

while True:
    try:
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        results = api.search(q="corona",lang="en")
        for result in results:
            print (str(result.id) + " " + result.text)
            insertTweet=(""" INSERT INTO [Coronavirus].[dbo].[Tweets]
                        VALUES({},'{}','{}','{}')""").format(result.id,result.text,"NULL","NULL")
    except Exception as e:
        print(str(e))
        continue
