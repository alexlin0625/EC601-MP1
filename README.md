# EC601-MP1/MP3
Boston University
EC601 Mini-Project 1 + Mini-Project 3 

Copyright Alex Jeffrey Lin 

### Status
[![Build Status](https://travis-ci.org/simkimsia/UtilityBehaviors.png)](https://travis-ci.org/simkimsia/UtilityBehaviors)

Table of contents
=================
<!--ts-->
   * [Mini-Project](#Mini-Project)
   * [Preparation](#Preparation)
   * [Installation](#Installation)
   * [Twitter.py](#Twitter.py) 
      * [get_all_tweets(screen_name)](#get-all-tweets(screen_name))
      * [labelPic(numa)](#downloadPic(numa))
      * [tweetsvideo()](#tweetsvideo())
   * [Mysql.py](#Mysql.py)
<!--te-->

Mini Project
================
The goal of this project is to create a library(in Python) that downloads images from random twitter user's feed, 
covert them into video and describe the contents of the images in the video using google vision. The entire program is done in Python. 

second part of this project is to implement databases into our twitter APi program. The purpose is to learn how to store information into databases such as total pictures of twitter download, image url, user ID, etc. The two databases that we will be implementing are MySQL and MongoDB. We can know the diffrence between relational DB and non-relational DB in this project.

Preparation
============
Before you use this code, you need to apply developer account for twitter. If you are a student, apply the developver account using school email will be approved immediately. Once it's approved, you can enter your consumer and access keys in the head of the twitter.py file. Now you can access the Twitter API. 

You also need to create a google cloud service account. Step by step tutorial on Google Cloud Vision API can be found in the following link. https://cloud.google.com/vision/docs/. You can set up authentication by creating a service account key. A JSON file that contains your key downloads to your computer. Lastly, you need to set the following statement in your terminal to pass the Google Authentication.
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="Enter your JSON file's PATH"
```
After successful running the progam, you should download and install databases to your local computer. The two databaese that will be using here is MySQL and MongoDB. After databases are installed, you should make sure you turn the server on. MySQL and MongoDB are both written using packages "pymysql" and "pymongo" to be competable with our twitter.py file. You can just import your databases.

Installation package
====================
```bash
$ PIL
$ tweepy 
$ wget
$ google.cloud
$ google.cloud.vision
$ ffmpeg (brew install ffmpeg)
$ pymysql
$ pymongo
```
Twitter.py
==========


**get_all_tweets(screen_name)**

  * After authorization, the system will download images from twitter user's feed.
  * The downloaded photos are renamed in number order with following code. I renamed the files in number order is to make ffmpeg easier to track the path of the downloaded pictures and labeling order in 
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


**labelPic(numa)**
  * Following for loop allows google vision to label downloaded photos in number order until it's over. 
```bash
path = os.getcwd()
    for i in range(1, numa):
        file_name_jpg = path+"/"+str(i)+".jpg"
        file_name = os.path.join(
            os.path.dirname(__file__),
            file_name_jpg)
```
  * Following code allows google vision to label tags that are visualizable on each photos
```bash
    img = Image.open(file_name_jpg)

    draw = ImageDraw.Draw(img)
    draw.text((0, 0), str(labels), (255, 255, 255))
    
    img.save(str(i)+".jpg")
```


**tweetsvideo()**
  * Following code coverts tagged photos into a video in mp4 format
```bash
ffmpeg_out = 'ffmpeg -framerate 0.20 -i %d.jpg output.mp4 '
    subprocess.call(ffmpeg_out, shell=True)
```
Mysql.py
==========

