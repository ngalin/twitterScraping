# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 10:11:15 2014

@author: ngalin
"""

#Tweet class

class Tweet:
  #number of tweets:
  count = 0

  def __init__(self,id):
    self.id = id
    self.user_handle = None
    self.user_name = None
    self.is_reply = None
    self.has_parent = None
    self.time = None
    self.text = None
    self.mentions = None
    self.links = None
    self.favorite = None
    self.retweets = None
    self.image_url = None
    Tweet.count += 1


  def displayNumTweets(self):
    print "Total Number of Tweets:" + Tweet.count

  def displayTweet(self):
    print "Tweet " + self.id + ", entries are:"
    print "time of tweet: " + self.time
    print "user handle: " + self.user_handle
    print "user name: " + self.user_name
    print "user_img: " + self.image_url
    print "tweet text: " + self.text
    print "mentions: " + self.mentions
    print "links to: " + self.links
    print "number favorites: " + self.favorite
    print "number retweets: " + self.retweets
    print "is tweet in reply: " + self.is_reply
    print "does tweet have parent: " + self.has_parent

