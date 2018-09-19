#!/usr/bin/env python
# encoding: utf-8
# Author - Alex Jeffrey Lin

import os 
import tweepy  
import subprocess

# Twitter API credentials
consumer_key = "enter your consumer_key"
consumer_secret = "enter your consumer_secret"
access_key = "enter your access_key"
access_secret = "enter your access_secret"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    print("at first:" + str(len(alltweets)))

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if len(alltweets) > 25:
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))


    # download images into files
    num = 1
    for tweets in alltweets:
        media = tweets.entities.get('media', [])
        if len(media) > 0:
            cmd = "wget -c "+"'"+media[0]['media_url']+"' -O " + str(num)+".jpg"
            os.system(cmd)
            num +=1
            #wget.download(media[0]['media_url'])

def tweetsvideo():
    #constructing videos with downloaded photos
    ffmpeg_out = 'ffmpeg -framerate 0.25 -i %d.jpg output.mp4 '
    subprocess.call(ffmpeg_out, shell=True)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@Ibra_official")
    tweetsvideo()
