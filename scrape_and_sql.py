# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import psycopg2
import twitterAPIaccess_ver5 as getTweets


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
args = getTweets.getCommandLineArgs(sys.argv)

matchPattern = args[0]
fromTime = args[1]
untilTime = args[2]

#con = None
#
#try:
#
#  con = psycopg2.connect(database='testdb' host='localhost')
#  cur = con.cursor()
#  cur.execute('SELECT version()')
#  ver = cur.fetchone()
#  print ver
#
#except psycopg2.DatabaseError, e:
#  print 'Error %s' % e
##  sys.exit()
#
#finally:
#
#  if con:
#    con.close()




listOfTweets = getTweets.scrapeTweets(matchPattern,fromTime,untilTime)

for tweet in listOfTweets:
  tweet.printTweet()
