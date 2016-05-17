import twitter
import json
import re
import time

CONSUMER_KEY = 'XxMdiXKvEY47BnPmx0hZDt3ei'
CONSUMER_SECRET = 'mQNZJrcDkjxzLWHx92V4e4OAafrixZCRF55QSJ0tJfW08BfqKD'
OAUTH_TOKEN = '75594277-r4OUo06P09RKQrsYJ4KY3eidk85UjHJI3GoC1TZj0'
OAUTH_TOKEN_SECRET = 'geqgBlYiB5120wyj3C1ei57KwVevdmAVaHlmpauccfLDj'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
# Nothing to see by displaying twitter_api except that it's now a
# defined variable
def purge_dublicates(X):
    unique_X = []
    for i, row in enumerate(X):
        if row not in X[i + 1:]:
            unique_X.append(row)
    return unique_X

tweet_string1 = ''
tweet_string2 = ''

print (twitter_api)

output_dir = 'E:\\Data\\_Code\\TestApiTwitter_1\\Data\\'
founded_today_file_name = output_dir + time.strftime("retweets_%Y-%m-%d.txt")
no_retweets_today_file_name = output_dir + time.strftime("no_retweets_%Y-%m-%d.txt")
not_founded_today_file_name = output_dir + time.strftime("retweets_not_founded_%Y-%m-%d.txt")
# Read in your ugly text file.
tweet_string = open('E:\Data\_Code\TestApiTwitter_1\Data\F2016_05_08.txt', 'rU')
retweets_file = open(founded_today_file_name, 'a')
retweets_not_found_file = open(not_founded_today_file_name, 'a')
no_retweets_found_file = open(no_retweets_today_file_name, 'a')
tweet_string = tweet_string.read()

# Find all the id numbers with a regex.
id_finder = re.compile(",\"id\":([0-9]{18,})")

# Go through the twee_string object and find all
# the IDs that meet the regex criteria.
idList = re.findall(id_finder, tweet_string)
idList = purge_dublicates(idList)

tweet_list = []

for id in idList:
    print(id)
    try:
        rt = twitter_api.statuses.retweets(_id=id)
        print(json.dumps(rt, indent=1))
        if rt:
            retweets_file.write(json.dumps(rt, indent=1))
            retweets_file.write("\n")
        else:
            print("No tweets found")
            no_retweets_found_file.write(id)
            no_retweets_found_file.write("\n")
    except twitter.api.TwitterHTTPError as te:
        if te.e.code == 404:
            print("tweet not found")
            retweets_not_found_file.write(id)
            retweets_not_found_file.write("\n")
        else:
            print(te)
            break


retweets_file.close()
no_retweets_found_file.close()
retweets_not_found_file.close()

        #tweet_string_new.write(twitter_api.statuses.retweeters.ids(_id=id)['ids']+'\n')
    #tweet_string_new = open('E:\Data\_Code\TestApiTwitter_1\Data\F2016_05_08.txt', 'rU')
    #tweet = twitter_api.get_status(id)
    #tweet_list.append(tweet)



# print ("""User IDs for retweeters of a tweet by @fperez_org
# that was retweeted by @SocialWebMini  ng and that @jyeee then retweeted
# from @SocialWebMining's timeline\n""")
# print (twitter_api.statuses.retweeters.ids(_id=334188056905129984)['ids'])
# print (json.dumps(twitter_api.statuses.show(_id=334188056905129984), indent=1))
# print
# print ("@SocialWeb's retweet of @fperez_org's tweet\n")
# print (twitter_api.statuses.retweeters.ids(_id=345723917798866944)['ids'])
# print (json.dumps(twitter_api.statuses.show(_id=345723917798866944), indent=1))
# print
# print ("@jyeee's retweet of @fperez_org's tweet\n")
# print (twitter_api.statuses.retweeters.ids(_id=338835939172417537)['ids'])
# print (json.dumps(twitter_api.statuses.show(_id=338835939172417537), indent=1))

