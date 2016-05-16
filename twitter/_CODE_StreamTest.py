import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

auth2 = tweepy.OAuthHandler('XxMdiXKvEY47BnPmx0hZDt3ei', '')
auth2.set_access_token('75594277-r4OUo06P09RKQrsYJ4KY3eidk85UjHJI3GoC1TZj0', '')
api = tweepy.API(auth2)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = auth2, listener=myStreamListener)
myStream.filter(track=['lmvilchesb'])


# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = auth, listener=myStreamListener())
# myStream.filter(track=['colombia'])