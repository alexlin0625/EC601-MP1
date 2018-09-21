# EC601-MP1
Boston University
EC601 Mini-Project 1 

Copyright Alex Jeffrey Lin 

Table of contents
=================
<!--ts-->
   * [API Mini-Project](#API-Mini-Project)
   * [Preparation](#Preparation)
   * [Installation](#Installation)
   * [Twitter.py](#Twitter.py) 
      * [get_all_tweets(screen_name)](#get-all-tweets(screen_name))
      * [tweetsvideo()](#tweetsvideo())
      * [downloadPic(numa)](#downloadPic(numa))
   * [Tests](#tests)
   * [Dependency](#dependency)
<!--te-->

API Mini-Project
================
The goal of this project is to create a library(in Python) that downloads images from random twitter user's feed, 
covert them into video and describe the contents of the images in the video using google vision. The entire program is done in Python

Preparation
============
Before you use this code, you need to apply developer account for twitter. If you are a student, apply the developver account using school email will be approved immediately. Once it's approved, you can enter your consumer and access keys in the head of the twitter.py file. Now you can access the Twitter API. 

You also need to create a google cloud service account. Step by step tutorial on Google Cloud Vision API can be found in the following link. https://cloud.google.com/vision/docs/. You can set up authentication by creating a service account key. A JSON file that contains your key downloads to your computer. Lastly, you need to set the following statement in your terminal to pass the Google Authentication.
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="Enter your JSON file's PATH"
```
Installation package
====================
```bash
$ PIL
$ tweepy 
$ wget
$ google.cloud
$ google.cloud.vision
$ ffmpeg (brew install ffmpeg)
```
Twitter.py
==========
get_all_tweets(screen_name)

  * After authorization, the system will download images from twitter user's feed.
  * The downloaded photos are renamed in number order with following code
```bash
num = 1
    for tweets in alltweets:
        media = tweets.entities.get('media', [])
        if len(media) > 0:
            # download images using wget command
            cmd = "wget -c "+"'"+media[0]['media_url']+"' -O " + str(num)+".jpg"
            os.system(cmd)
            num += 1
    return num
```
I renamed the files in number order is to make ffmpeg easier to track the path of the downloaded pictures and 
  * rename files in number olders such as 1.jpg format.
  
2) tweetsvideo()
  * Following code coverts downloaded pictures into 
  
3) downloadPic(numa)
