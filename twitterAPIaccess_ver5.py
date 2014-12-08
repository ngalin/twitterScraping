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

#definitions for json structure returned from twitter search api:
get_tweet_description = 'js-stream-item'
max_tweet_metadata_entries = 50
user_twitter_handle = 'data-screen-name'
user_actual_name = 'data-name'
user_twitter_id = 'data-user-id'
user_replying = 'data-is-reply-to'
user_tweet_has_parent = 'data-has-parent-tweet'
user_tweet_time = 'time'

#for each day of the year, compile a query and download tweets:
start_day_sec = 1388534400
end_day_sec = 1419984000 #31/DEC/2014
end_day_sec = 1417824000 #06/DEC/2014

sec_in_day = 86400
end_day_sec = start_day_sec + sec_in_day*1
days_of_tweets = 365

from_day_sec = start_day_sec
until_day_sec = from_day_sec + sec_in_day
text = [[0 for i in range(max_tweet_metadata_entries)] for j in range(days_of_tweets)]
num_tweets_per_day = [0 for i in range(days_of_tweets)]
times_ms = [[0 for i in range(max_tweet_metadata_entries)] for j in range(days_of_tweets)]
idx_day = 0

#regular expression compilation
p1 = re.compile('data-time=\"\d+')
p2 = re.compile('\d+')

while (from_day_sec <= end_day_sec):
  query = 'https://twitter.com/i/search/timeline?f=realtime&q=%22uber_sydney%22%20since%3A'+str(from_day_sec)+'%20until%3A'+str(until_day_sec)+'&src=typd'

  response = urllib2.urlopen(query)
  data = json.load(response)
  soup = bs(str(data))

  tweets = soup.findAll('li',get_tweet_description)
  num_tweets_per_day[idx_day] = len(tweets)
  for idx,tweet in enumerate(tweets):
    print idx
    tweet_soup = bs(str(tweet))

    tmp = tweet_soup.findAll('div',{user_twitter_handle:True})
    print tmp[0][user_twitter_handle]
    tmp = tweet_soup.findAll('div',{user_actual_name:True})
    print tmp[0][user_actual_name]
    tmp = tweet_soup.findAll('div',{user_twitter_id:True})
    print tmp[0][user_twitter_id]
    tmp = tweet_soup.findAll('div',{user_replying:True})
    if bool(tmp):
      print tmp[0][user_replying]
    tmp = tweet_soup.findAll('div',{user_tweet_has_parent:True})
    if bool(tmp):
      print tmp[0][user_tweet_has_parent]
    tmp = tweet_soup.findAll('small',{'class':user_tweet_time})
    tmp = p1.findall(str(tmp))
    print p2.findall(str(tmp))

  idx_day = idx_day+1
  from_day_sec = from_day_sec + sec_in_day