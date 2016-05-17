import tweepy

auth = tweepy.OAuthHandler('XxMdiXKvEY47BnPmx0hZDt3ei', '')
auth.set_access_token('75594277-r4OUo06P09RKQrsYJ4KY3eidk85UjHJI3GoC1TZj0', '')

api = tweepy.API(auth)
user = api.get_user('gabrielmoreno10')
#print(user)
print (user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)

api.user_timeline(id="gabrielmoreno10")

for status in tweepy.Cursor(api.user_timeline, id="gabrielmoreno10").items():
    # process status here
    print(status.text)
