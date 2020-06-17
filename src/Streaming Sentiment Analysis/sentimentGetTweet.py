from tweepy import Stream
from textblob import TextBlob
import json
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

## API KEY
ckey="XXXXXXXXXX"
csecret="XXXXXXXXXX"
atoken="XXXXXXXXXX"
asecret="XXXXXXXXXX"

class listener(StreamListener):
    
    def on_data(self, data):
        #Gelen datanın json formatına çevrilmesi.
        all_data=json.loads(data)
        tweet=all_data["text"]
        #Textblob'tan sentiment analizi
        tweet=TextBlob(tweet)
        #Grafikte pozitif ve negatif esas alındığı için tekrardan 2 ye ayrılmamıştır.
        if tweet.sentiment.polarity > 0:
            sentimentResult="positive"
        elif tweet.sentiment.polarity == 0:
            sentimentResult="neutral"
        else:
            sentimentResult="negative"
        #Analiz edilenler twitter-out.txt'ye yazılmaktadır.
        output=open("twitter-out.txt","a")
        output.write(sentimentResult+" "+ str(tweet.sentiment.polarity))
        output.write('\n')
        output.close()

        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
#Gelen dataları filtre yöntemi ile covid-19 tweetlerini ayırıyoruz.
twitterStream = Stream(auth, listener())
twitterStream.filter(languages=["en"], track=["covid-19"])


