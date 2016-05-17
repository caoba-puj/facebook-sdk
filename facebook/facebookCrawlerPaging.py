# -*- coding: utf-8 -*-
import facebook
import json
import requests
import web
import time
from facepy import GraphAPI
from facepy import utils
from urlparse import parse_qs

#

#Crear Archivos
postsFile = open('Data/posts.txt', 'w')
likesFile = open('Data/likes.txt', 'w')
commentsFile = open('Data/comments.txt', 'w')

app_id = "916717871760512"
app_secret="92d85a8f6d3768b1e1d76d046b27e1c8"
post_login_url="http://0.0.0.0:8080/"

#Acceso a Facebook
token = utils.get_application_access_token(app_id, app_secret)
#token = "EAACEdEose0cBAAEOTkPTkbfZBOzwJye83bZAm9xU4VZC4CgC0dK6DSH17UMrcUBxZCQMFLZAN5grg01NjtyJjVTm0pmsmZCcUY0ZAezC8Pp1DWLzTztJmamK7FZC5rulZBd3VgMDVkon5NjFBlPVt9R3QvTgHHpxbxJnhAHAIizRBXAZDZD"
graph = facebook.GraphAPI(access_token=token, version='2.2')

"""
def pruebaUsuario():
    #10151981468682251 Marco Lozano Sierra
    #10204409256658491
    #picture = graph.get_object("10151981468682251/picture")
    #print picture["url"]

    picture = graph.get_object("10151407860159534/picture")
    print picture
    pruebaUsuario()
"""
#profile = graph.get_object("chocolatesjet")
profile = graph.get_object("hamburguesaselcorral")

#posts = graph.get_object(profile['id']+"/posts",since='2010-01-01', until='2015-01-01',limit=50)
posts = graph.get_object(profile['id']+"/posts?fields=likes,comments,message")

start = time.time()
def getLikes(likes):
    try:
        while(True):
            likesFile = open('Data/likes.txt', 'a')
            JDictLikes= json.loads(json.dumps(likes))
            for like in JDictLikes['data']:
                #likeProfile = graph.get_object(like['id'])

                likesFile.write(json.dumps(like)+"\n")

            likes=requests.get(likes['paging']['next']).json()
    except KeyError:
        print "Error in Likes"
        likesFile.write("\n")
        print "Tiempo transcurrido [" + time.time() + "]"
        likesFile.close()

def getComments(comments):
    try:
        while(True):
            commentsFile = open('Data/comments.txt', 'a')
            JDictComments= json.loads(json.dumps(comments))

            for comment in JDictComments['data']:

                commentsFile.write(json.dumps(comment)+"\n")

            #if "next" in comments['paging']:
            comments=requests.get(comments['paging']['next']).json()
    except Exception as e:
        print "Error in Comments"
        commentsFile.write("\n")
        print "Tiempo transcurrido [" + time.time() + "]"
        commentsFile.close()



try:
    while(True):
        postsFile = open('Data/posts.txt', 'a')
        JDictPosts = json.loads(json.dumps(posts))
        for post in JDictPosts['data']:
            if "message" in post:
                postsFile.write(json.dumps(post)+"\n")

                if "likes" in post:
                    likes = post['likes']
                    getLikes(likes)

                if "comments" in post:
                    comments = post['comments']
                    getComments(comments)

        posts=requests.get(posts['paging']['next']).json()

except Exception as e:
    print "Error in post: "
    postsFile.close()
    print "Tiempo transcurrido ["+time.time()+"]"
print "Información guardada!"
end = time.time()
print "Tiempo Total: "+(end - start)
