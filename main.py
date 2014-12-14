# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scraper
import getDefaults as gd

def getCommandLineArgs(args): #move to 'main', and rename twitterScraper as 'main.py'
  if (len(args) == 4):
    matchPattern = args[1]
    print >> sys.stderr, matchPattern
    fromTime = int(args[2])
    untilTime = int(args[3])
  else:
    matchPattern = gd.getMatchPattern()
    times = gd.getTimestampBounds()
    fromTime = times[0]
    untilTime = times[1]
    print >> sys.stderr, "Didn't specify, or, have incorrect number of command line args."
    print >> sys.stderr, "Using default: "
    print >> sys.stderr, "matchPattern: " + matchPattern
    print >> sys.stderr, "From time: " + str(fromTime) + " to: " + str(untilTime)

  return matchPattern, fromTime, untilTime

print >> sys.stderr, 'Number of arguments:', len(sys.argv), 'arguments.'
print >> sys.stderr, 'Argument List:', str(sys.argv)
args = getCommandLineArgs(sys.argv)

matchPattern = args[0]
fromTime = args[1]
untilTime = args[2]

for tweet in scraper.scrapeTweets(matchPattern,fromTime,untilTime):
    print tweet

