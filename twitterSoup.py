# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:18:49 2014

@author: ngalin
"""
from bs4 import BeautifulSoup as bs
import re
import sys
from Tweet import Tweet
import html2text

#definitions for json structure returned from twitter search api:
class Tags:
    getTweet = 'js-stream-item'
    handle = 'data-screen-name'
    name = 'data-name'
    id = 'data-user-id'
    isreply = 'data-is-reply-to'
    hasparent = 'data-has-parent-tweet'
    time = 'time'
    mentions = 'data-mentions'
    links = 'js-details'
    text = 'js-tweet-text'
    replies = 'ProfileTweet-actionCountForAria'
    retweets = 'ProfileTweet-actionCountForAria'
    favorites = 'ProfileTweet-actionCountForAria'

def get_tweet_soups(soup):
    return soup.findAll('li',Tags.getTweet)

def buildQuery(matchPattern,fromTime,untilTime):
  return 'https://twitter.com/i/search/timeline?f=realtime&q=%22'+matchPattern+'%22%20since%3A'+str(fromTime)+'%20until%3A'+str(untilTime)+'&src=typd'

def getTime(tweet):
  soup = bs(str(tweet))
  p1 = re.compile('data-time=\"\d+')
  p2 = re.compile('\d+')
  tmp = soup.findAll('small',{'class':'time'})
  tmp = p1.findall(str(tmp))
  tmp = p2.findall(str(tmp))
  return int(tmp[0])

def buildTweet(tweet_soup): #separate into two functions - build the tweet, and have caller add tweet to list - return tweet
  soup = bs(str(tweet_soup)) #double check that need to 'resoup'
  a_tweet = Tweet(getTweetId(soup))
  populateTweetFields(a_tweet,soup)
  return a_tweet

def getTweetId(soup):
  tmp = soup.findAll('div',{Tags.id:True})
  print >> sys.stderr, tmp[0][Tags.id]
  return tmp[0][Tags.id]

def populateTweetFields(a_tweet,soup):
  a_tweet.user_handle = getTweetHandle(soup)
  a_tweet.user_name = getTweetName(soup)
  a_tweet.time = getTweetTime(soup)
  a_tweet.text = getTweetText(soup)
  a_tweet.mentions = getTweetMentions(soup)
  a_tweet.links = getTweetLinks(soup)
  a_tweet.image_url = getTweetImageUrl(soup)
  a_tweet.favorites = getNumFavorites(soup)
  a_tweet.retweets = getNumRetweets(soup)
  a_tweet.reply = getNumReplies(soup)
  a_tweet.is_reply = getTweetReply(soup)
  a_tweet.has_parent = getTweetParent(soup)
 # a_tweet.printTweet()
 # print a_tweet

def getTweetHandle(soup):
  tmp = soup.findAll('div',{Tags.handle:True})
  #print tmp[0][user_handle]
  return str(tmp[0][Tags.handle])

def getTweetName(soup):
  tmp = soup.findAll('div',{Tags.name:True})
  return str(tmp[0][Tags.name])

def getTweetReply(soup):
  tmp = soup.findAll('div',{Tags.isreply:True})
  if bool(tmp):
    return bool(tmp[0][Tags.isreply])
  else:
    return False

def getTweetParent(soup):
  tmp = soup.findAll('div',{Tags.hasparent:True})
  if bool(tmp):
    return bool(tmp[0][Tags.hasparent])
  else:
    return False

def getTweetTime(soup):
  p1 = re.compile('data-time=\"\d+')
  p2 = re.compile('\d+')
  tmp = soup.findAll('small',{'class': Tags.time})
  tmp = p1.findall(str(tmp))
  tmp = p2.findall(str(tmp))
  return int(tmp[0])

def getTweetMentions(soup):
   tmp = soup.findAll('div',{Tags.mentions:True})
   if bool(tmp):
     return tmp[0][Tags.mentions]
   else:
     return ''

def getTweetText(soup):
  tweet_text = soup.findAll('p', Tags.text)
  h = html2text.html2text(str(tweet_text))
  h = h.replace('****','')
  h = h.replace('***','')
  h = h.replace('**','')
  return h.replace('\n','')

def getTweetImageUrl(soup):
  image_url = soup.findAll('img',src=True)
  return str(image_url[0]['src'])

def getTweetLinks(soup):
  tweet_links = soup.findAll('a', Tags.links)
  return str(tweet_links)

def getNumReplies(soup):
  num = soup.findAll('span',{'class': Tags.replies})[0]
  p = re.compile('\d+')
  tmp = p.findall(str(num))
  return int(tmp[0])

def getNumRetweets(soup):
  num = soup.findAll('span',{'class': Tags.retweets})[1]
  p = re.compile('\d+')
  tmp = p.findall(str(num))
  return int(tmp[0])

def getNumFavorites(soup):
  num = soup.findAll('span',{'class': Tags.favorites})[2]
  p = re.compile('\d+')
  tmp = p.findall(str(num))
  return int(tmp[0])
