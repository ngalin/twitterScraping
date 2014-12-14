# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""
import json
import urllib2
from bs4 import BeautifulSoup as bs
import twitterSoup as ts
import re
import sys

def scrapeTweets(matchPattern,fromTime,untilTime): #generator of tweets
  #definitions for json structure returned from twitter search api:
  #initialisation of return values:
  num_tweets_scraped = 0
  finished = False

  while not finished:
    #print "Query times: " + str(fromTime) + " to " + str(untilTime)
    print >> sys.stderr, "Query times: " + str(fromTime) + " to " + str(untilTime)
    query = ts.buildQuery(matchPattern,fromTime,untilTime)
    response = urllib2.urlopen(query)
    data = json.load(response)
    soup = bs(str(data))

    tweet_soups = ts.get_tweet_soups(soup)
    num_tweets_scraped = num_tweets_scraped + len(tweet_soups)

    for tweet_soup in tweet_soups:
      if not re.search('Related Searches:',str(bs(str(tweet_soup)))):
        yield ts.buildTweet(tweet_soup)

    if len(tweet_soups):
      untilTime = ts.getTime(tweet_soups[-1]) #get time of last tweet
    else:
      print >> sys.stderr, 'Finished getting all tweets, total: ' + str(num_tweets_scraped)
      finished = True
