import facebook # pip install facebook-sdk
import json
# A helper function to pretty-print Python objects as JSON
def pp(o):
    print(json.dumps(o, indent=1))

# Create a connection to the Graph API with your access token
#To obtain the access token enter to the url: https://developers.facebook.com/tools/explorer
accessToken=''
g = facebook.GraphAPI(access_token=accessToken, version='2.2')
# Execute a few sample queries
print('---------------')
print('Me')
print('---------------')
pp(g.get_object('me'))
print()
print('---------------')
print('My Friends')
print('---------------')
pp(g.get_connections('me', 'friends'))
print()
print('---------------')
print('Social Web')
print('---------------')
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))

# Get an instance of Mining the Social Web
# Using the page name also works if you know it.
# e.g. 'miningTheSocialWeb' or 'CrossFit'
#hamburguesaselcorral
mtsw_id = '146803958708175'
pp(g.get_object(mtsw_id))

# MTSW catalog link
pp(g.get_object('http://shop.oreilly.com/product/0636920030195.do'))
# PCI catalog link
pp(g.get_object('http://shop.oreilly.com/product/9780596529321.do'))