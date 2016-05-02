import facebook # pip install facebook-sdk
import json

# A helper function to pretty-print Python objects as JSON
def pp(o):
    print(json.dumps(o, indent=1))

# Create a connection to the Graph API with your access token
accessToken = ''
g = facebook.GraphAPI(access_token=accessToken, version='2.2')

# Find Pepsi and Coke in search results
pp(g.request('search', {'q' : 'pepsi', 'type' : 'page', 'limit' : 5}))
pp(g.request('search', {'q' : 'coke', 'type' : 'page', 'limit' : 5}))

pepsi_id = '56381779049' # Could also use 'PepsiUS'
coke_id = '40796308305' # Could also use 'CocaCola'
# A quick way to format integers with commas every 3 digits
def int_format(n): return "{:,}".format(n)
print("Pepsi likes:", int_format(g.get_object(pepsi_id)['likes']))
print("Coke likes:", int_format(g.get_object(coke_id)['likes']))

pp(g.get_connections(pepsi_id, 'feed'))
pp(g.get_connections(pepsi_id, 'links'))
pp(g.get_connections(coke_id, 'feed'))
pp(g.get_connections(coke_id, 'posts'))