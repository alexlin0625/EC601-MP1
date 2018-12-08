#!/usr/bin/env python
# encoding: utf-8
# Author - Alex Jeffrey Lin

import pymongo
import datetime
import os


def mymongodb(Username, twtnum, picnum, picurl, time, tag):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["minipj3"]
    collect = db[tablename]
    dblist = client.list_database_names()

    time = datetime.datetime.now()
    mydict = {'User_ID':Username,'Twt_num': twtnum, 'Pic_total': picnum, 'Pic_url': picurl, 'Time':time, 'Tag':tag,}

    x = collect.insert_one(mydict)
    collist = db.list_collection_names()


def search(tablename, key):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["minipj3"]
    collect = db[tablename]
    quiry = {"tags": {"$regex": ".*%s.*" % key}}
    result = collect.find(quiry)
    result1 = collect.find_one(quiry)
    if result1 is None:
        print('Keyword %s is not found in collection %s (MongoDB)' %(key, tablename))
    else:
        print('Keyword %s founded in collection %s below (MongoDB):' %(key, tablename))
        for a in result:
            print(a)


if __name__ == '__main__':
    mymongodb('Alexlin', 20, 15, 'www.google.com', '12am', 15)
    search('twitter','input')