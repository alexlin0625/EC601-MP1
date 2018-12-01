#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:54:51 2018

@author: AlexLin
"""

import pymysql
#import datetime

def connectdb():
    # connect to MySQL database
    db = pymysql.connect("localhost", "root", "@Alixpig6", "mysql_a")
    print('connected')
    return db

def createtable(db):
    cursor = db.cursor()

    # create tables along with columns
    sql = """CREATE TABLE minipj3 (
            User_ID CHAR(30) NOT NULL,
            Twt_num INT,
            Pic_total INT,
            Pic_url CHAR(100),
            Time CHAR(50),
            Tag INT )"""

    cursor.execute(sql)

def insertdb(db):
    cursor = db.cursor()
    time = db.datatime.datatime

    # insert values into the table
    sql = """INSERT INTO minipj3(User_ID, Twt_num, Pic_total, Pic_url, Time, Tag)
    VALUES ('%s', %s, %s, '%s', '%s', %s)%
         #('Username', twtnum, picnum, picurl, time , tag)"""

    #sql = """INSERT INTO minipj3
          #VALUES ('Alexlin', 20, 15, 'www.google.com', '12am', 15)"""
    try:
        cursor.execute(sql)

        db.commit()

    except:
        # Rollback in case there is any error
        print('inserting failed')
        db.rollback()

def querydb(db):
    cursor = db.cursor()

    sql = "SELECT * FROM minipj3"
    try:
        cursor.execute(sql)
        # obtain all the records
        results = cursor.fetchall()
        for row in results:
            User_ID = row[0]
            Twt_num = row[1]
            Pic_total = row[2]
            Pic_url = row[3]
            Time = row[4]
            Tag = row[5]

            # print the results
            print("User_ID: '%s', Twt_num: %s, Pic_total: %s, Pic_url: '%s', Time: '%s', Tag: %s" %
                  (User_ID, Twt_num, Pic_total, Pic_url, Time, Tag))
    except:
        print("Error: unable to fecth data")

def main():
    db = connectdb()    # connect MySQL database
    createtable(db)     # create table
    insertdb(db)        # insert values
    querydb(db)         # obtain records

if __name__ == '__main__':
    main()


