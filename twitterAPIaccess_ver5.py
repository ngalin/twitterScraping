# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""
import json
import urllib2
from bs4 import BeautifulSoup as bs
import helperFunctions as hf

def getCommandLineArgs(args):
  if (len(args) == 4):
    matchPattern = args[1]
    print matchPattern
    fromTime = int(args[2])
    untilTime = int(args[3])
  else:
    matchPattern = hf.getMatchPattern()
    times = hf.getTimestampBounds()
    fromTime = times[0]
    untilTime = times[1]
    print "Didn't specify, or, have incorrect number of command line args."
    print "Using default: "
    print "matchPattern: " + matchPattern
    print "From time: " + str(fromTime) + " to: " + str(untilTime)

  return matchPattern, fromTime, untilTime

def scrapeTweets(matchPattern,fromTime,untilTime):
  #definitions for json structure returned from twitter search api:
  get_tweet_description = 'js-stream-item'
  #initialisation of return values:
  num_tweets_scraped = 0
  finished = False
  listOfTweets = list()
  while not finished:
    print "Query times: " + str(fromTime) + " to " + str(untilTime)
    query = hf.buildQuery(matchPattern,fromTime,untilTime)
    response = urllib2.urlopen(query)
    data = json.load(response)
    soup = bs(str(data))
    tweets = soup.findAll('li',get_tweet_description)
    num_tweets_scraped = num_tweets_scraped + len(tweets)

    for tweet in tweets:
      #print hf.getTime(tweet)
      hf.addTweet2List(listOfTweets,tweet)

    if (len(tweets) > 0):
      untilTime = hf.getTime(tweets[-1]) #get time of last tweet
    else:
      print 'Finished getting all tweets, total: ' + str(num_tweets_scraped)
      finished = True

  return listOfTweets