# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:18:49 2014

@author: ngalin
"""
from bs4 import BeautifulSoup as bs
import re
MAX_TWEETS_PER_QUERY = 0

def getTimestampBounds():
  #for each day of the year, compile a query and download tweets:
  start_day_sec = 1388534400
  #end_day_sec = 1419984000 #31/DEC/2014
  #end_day_sec = 1417824000 #06/DEC/2014

  sec_in_day = 86400
  end_day_sec = start_day_sec + sec_in_day*5
  #days_of_tweets = 365

  from_day_sec = start_day_sec
  until_day_sec = end_day_sec#from_day_sec + sec_in_day
  return from_day_sec, until_day_sec


def getMatchPattern():
  return 'uber_sydney'


def buildQuery(matchPattern,fromTime,untilTime):
  return 'https://twitter.com/i/search/timeline?f=realtime&q=%22'+matchPattern+'%22%20since%3A'+str(fromTime)+'%20until%3A'+str(untilTime)+'&src=typd'


def evaluate_end_condition(numTweets):
  if (numTweets == MAX_TWEETS_PER_QUERY):
    return True
  else:
    return False

def getTime(tweet):
  soup = bs(str(tweet))
  ##regular expression compilation
  p1 = re.compile('data-time=\"\d+')
  p2 = re.compile('\d+')
  tmp = soup.findAll('small',{'class':'time'})
  tmp = p1.findall(str(tmp))
  tmp = p2.findall(str(tmp))

  return int(tmp[0])