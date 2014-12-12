# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import getTweets


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
args = getTweets.getCommandLineArgs(sys.argv)

matchPattern = args[0]
fromTime = args[1]
untilTime = args[2]

listOfTweets = getTweets.scrapeTweets(matchPattern,fromTime,untilTime)

for tweet in listOfTweets:
  tweet.printTweet()


#
#
##debug:
#for idx,tweet in enumerate(listOfTweets):
#  print str(idx) + ' ' + tweet.links
#
#for tweet in listOfTweets:
#  print tweet.image_url