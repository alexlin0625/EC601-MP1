#!/usr/bin/env python
# encoding: utf-8
# Author - Alex Jeffrey Lin
import os

import tweepy  # https://github.com/tweepy/tweepy
import wget  # lib for downloading images into file
import subprocess

# Twitter API credentials
consumer_key = "UgOFDaoQ67TO25ELAlCn6AEPv"
consumer_secret = "bhhCvWlQWO8NburU28wNvAiixWDdHFuI9C8GjoAOqo9GUXIM28"
access_key = "1041455819269779456-7zSqv3Fm2L0hB4lrQISub64R57zxBB"
access_secret = "QffdxV2F4PUzlICRITkePTHjlmnIYE4Ks7vi0AzCdhtvA"


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


#constructing videos with downloaded photos
def tweetsvideo():
    ffmpeg_out = 'ffmpeg -framerate 0.25 -i %d.jpg output.mp4 '
    subprocess.call(ffmpeg_out, shell=True)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@Ibra_official")
    tweetsvideo()
