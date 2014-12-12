# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:18:49 2014

@author: ngalin
"""
from bs4 import BeautifulSoup as bs
import re
from Tweet import Tweet
MAX_TWEETS_PER_QUERY = 0

#definitions for json structure returned from twitter search api:
dictOfHTMLMatches = {'getTweet':'js-stream-item',
                     'handle':'data-screen-name',
                     'name':'data-name',
                     'id':'data-user-id',
                     'isreply':'data-is-reply-to',
                     'hasparent':'data-has-parent-tweet',
                     'time':'time',
                     'mentions':'data-mentions',
                     'links':'js-details',
                     'text':'js-tweet-text'}


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

def addTweet2List(listOfTweets,tweet):
  soup = bs(str(tweet))
  a_tweet = Tweet(getTweetId(soup))
  populateTweetFields(a_tweet,soup)
  print a_tweet.count
  listOfTweets.append(a_tweet)

def getTweetId(soup):
  user_twitter_id = dictOfHTMLMatches['id']
  tmp = soup.findAll('div',{user_twitter_id:True})
  return tmp[0][user_twitter_id]

def populateTweetFields(a_tweet,soup):
  a_tweet.user_handle = getTweetHandle(soup)
  a_tweet.user_name = getTweetName(soup)
  a_tweet.time = getTweetTime(soup)
  a_tweet.text = getTweetText(soup)
  a_tweet.mentions = getTweetMentions(soup)
  a_tweet.links = getTweetLinks(soup)
  a_tweet.image_url = getTweetImageUrl(soup)
  a_tweet.favorites = getTweetLinks(soup)
  a_tweet.retweets = getTweetLinks(soup)
  a_tweet.is_reply = getTweetReply(soup)
  a_tweet.has_parent = getTweetParent(soup)

def getTweetHandle(soup):
  user_handle = dictOfHTMLMatches['handle']
  tmp = soup.findAll('div',{user_handle:True})
  print tmp[0][user_handle]
  return tmp[0][user_handle]

def getTweetName(soup):
  user_name = dictOfHTMLMatches['name']
  tmp = soup.findAll('div',{user_name:True})
  return tmp[0][user_name]

def getTweetReply(soup):
  tweet_is_reply = dictOfHTMLMatches['isreply']
  tmp = soup.findAll('div',{tweet_is_reply:True})
  if bool(tmp):
    return tmp[0][tweet_is_reply]
  else:
    return False

def getTweetParent(soup):
  tweet_has_parent = dictOfHTMLMatches['hasparent']
  tmp = soup.findAll('div',{tweet_has_parent:True})
  if bool(tmp):
    return tmp[0][tweet_has_parent]
  else:
    return False

def getTweetTime(soup):
  time = dictOfHTMLMatches['time']
  p1 = re.compile('data-time=\"\d+')
  p2 = re.compile('\d+')
  tmp = soup.findAll('small',{'class':time})
  tmp = p1.findall(str(tmp))
  tmp = p2.findall(str(tmp))

  return int(tmp[0])

def getTweetMentions(soup):
   user_mentions = dictOfHTMLMatches['mentions']
   tmp = soup.findAll('div',{user_mentions:True})
   if bool(tmp):
     return tmp[0][user_mentions]
   else:
     return False

def getTweetText(soup):
  text = dictOfHTMLMatches['text']
  tweet_text = soup.findAll('p',text)
  return tweet_text

def getTweetImageUrl(soup):
  image_url = soup.findAll('img',src=True)
  return image_url[0]['src']

def getTweetLinks(soup):
  links = dictOfHTMLMatches['links']
  tweet_links = soup.findAll('a',links)
  return tweet_links
