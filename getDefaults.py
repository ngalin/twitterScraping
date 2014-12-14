__author__ = 'ngalin'
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:56:24 2014

@author: ngalin
"""


def getTimestampBounds(): #move
  start_day_sec = 1388534400
  sec_in_day = 86400
  end_day_sec = start_day_sec + sec_in_day*5
  from_day_sec = start_day_sec
  until_day_sec = end_day_sec

  return from_day_sec, until_day_sec


def getMatchPattern(): #move
  return 'uber'#'uber_sydney'