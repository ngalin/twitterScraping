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
    self.favorite = 0
    self.retweets = 0
    self.reply = 0
    self.image_url = None
    Tweet.count += 1


  def displayNumTweets(self):
    print "Total Number of Tweets:" + Tweet.count

  def displayTweet(self):
    print "Tweet " + self.id + ", entries are:"
    print "time of tweet: " + str(self.time)
    print "user handle: " + self.user_handle
    print "user name: " + self.user_name
    print "user_img: " + self.image_url
    print "tweet text: " + self.text
    print "mentions: " + str(self.mentions)
    print "links to: " + self.links
    print "number favorites: " + str(self.favorite)
    print "number retweets: " + str(self.retweets)
    print "number replies: " + str(self.reply)
    print "is tweet in reply: " + str(self.is_reply)
    print "does tweet have parent: " + str(self.has_parent)

  def printTweet(self):
    print str(self.id) + '\t' + \
      self.user_handle + '\t' + \
      self.user_name + '\t' + \
      self.image_url + '\t' + \
      str(self.time) + '\t' + \
      self.text + '\t' + \
      self.mentions + '\t' + \
      self.links + '\t' + \
      str(self.favorites) + '\t' + \
      str(self.retweets) + '\t' + \
      str(self.reply) + '\t' + \
      str(self.is_reply) + '\t' + \
      str(self.has_parent) + '\t'
