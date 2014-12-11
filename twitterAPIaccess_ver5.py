# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""

import twitter
import json
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import urllib2
from bs4 import BeautifulSoup as bs
import re
import html2text
import datetime
from helperFunctions import getTimestampBounds
from helperFunctions import getMatchPattern
from helperFunctions import buildQuery
from helperFunctions import evaluate_end_condition
from helperFunctions import getTime


#definitions for json structure returned from twitter search api:
get_tweet_description = 'js-stream-item'
max_tweet_metadata_entries = 50
max_tweets_per_page = 20
user_twitter_handle = 'data-screen-name'
user_actual_name = 'data-name'
user_twitter_id = 'data-user-id'
user_replying = 'data-is-reply-to'
user_tweet_has_parent = 'data-has-parent-tweet'
user_tweet_time = 'time'
user_mentions = 'data-mentions'


matchPattern = getMatchPattern();
times = getTimestampBounds();
fromTime = times[0]
untilTime = times[1]

#initialisation of return values:
num_tweets_scraped = 0
finished = False
while not finished:
  print "Times: " + str(fromTime) + " to " + str(untilTime)
  query = buildQuery(matchPattern,fromTime,untilTime)
  response = urllib2.urlopen(query)
  data = json.load(response)
  soup = bs(str(data))
  tweets = soup.findAll('li',get_tweet_description)
  num_tweets_scraped = num_tweets_scraped + len(tweets)

  print len(tweets)
  finished = evaluate_end_condition(len(tweets))

  if not finished:
    for tweet in tweets:
      print getTime(tweet)

    untilTime = getTime(tweets[-1]) #get time of last tweet
    #if (fromTime > untilTime):
    #  finished = True
  else:
    for tweet in tweets:
      print getTime(tweet)
      print 'Finished getting all tweets'

#
#  #clear various variables:
#  soup = None
#  tweets = None
#  response = None
#  query = None
#  data = None

#
#
#
#
#
#text = [[0 for i in range(max_tweet_metadata_entries)] for j in range(days_of_tweets)]
#num_tweets_per_day = [0 for i in range(days_of_tweets)]
#times_ms = [[0 for i in range(max_tweet_metadata_entries)] for j in range(days_of_tweets)]
#idx_day = 0;
#
#
#
#
#
##regular expression compilation
#p1 = re.compile('data-time=\"\d+')
#p2 = re.compile('\d+')
#
#while (from_day_sec <= end_day_sec):
#  query = 'https://twitter.com/i/search/timeline?f=realtime&q=%22uber_sydney%22%20since%3A'+str(from_day_sec)+'%20until%3A'+str(until_day_sec)+'&src=typd'
#
#  response = urllib2.urlopen(query)
#  data = json.load(response)
#  soup = bs(str(data))
#
#  tweets = soup.findAll('li',get_tweet_description)
#  num_tweets_per_day[idx_day] = len(tweets)
#
#
#
#
#
#
#
#
#
#
#
#  for idx,tweet in enumerate(tweets):
#    print idx
#    tweet_soup = bs(str(tweet))
#
#    tmp = tweet_soup.findAll('div',{user_twitter_handle:True})
#    print tmp[0][user_twitter_handle]
#    tmp = tweet_soup.findAll('div',{user_actual_name:True})
#    print tmp[0][user_actual_name]
#    tmp = tweet_soup.findAll('div',{user_twitter_id:True})
#    print tmp[0][user_twitter_id]
#    tmp = tweet_soup.findAll('div',{user_replying:True})
#    if bool(tmp):
#      print tmp[0][user_replying]
#    tmp = tweet_soup.findAll('div',{user_tweet_has_parent:True})
#    if bool(tmp):
#      print tmp[0][user_tweet_has_parent]
#    tmp = tweet_soup.findAll('small',{'class':user_tweet_time})
#    tmp = p1.findall(str(tmp))
#    print p2.findall(str(tmp))
#    tmp = tweet_soup.findAll('div',{user_mentions:True})
#    if bool(tmp):
#      print tmp[0][user_mentions]
#    image_link = tweet_soup.findAll('img',src=True)
#    print image_link[0]['src']
#    tweet_text = tweet_soup.findAll('p','js-tweet-text')
#    print tweet_text
#    tweet_timestamps = tweet_soup.findAll('a','tweet-timestamp')
#    print tweet_timestamps
#    tweet_links = tweet_soup.findAll('a','js-details')
#    print tweet_links
#
#  #look at the timestamp of last tweet, and re-run query if necessary (want to get all tweets for a given day)
#  if (len(tweets) < max_tweets_per_page):
#    tmp = tweet_soup.findAll('small',{'class':user_tweet_time})
#    tmp = p1.findall(str(tmp))
#    tmp = p2.findall(str(tmp))
#    last_timestamp = tmp[0]
#    new_query = 'https://twitter.com/i/search/timeline?f=realtime&q=%22uber_sydney%22%20since%3A'+last_timestamp+'%20until%3A'+str(until_day_sec)+'&src=typd'
#
#
#
#    idx_day = idx_day+1
#  from_day_sec = from_day_sec + sec_in_day