twitterScraping
===============

Scraping the html from: twitter.com/i/search to get all historical tweets

Input: 
- search term/string [string]
- from time: unix timestamp [int]
- until time: unix timestamp [int]

Output (returns all tweets that match the search term, during the specified time period):
- # of tweets scraped for the time period
- tweets:
  [user twitter handle, string]
  [user name, string]
  [user twitter id, int]
  [is tweet in reply to another?, bool]
  [does tweet have a parent?, bool]
  [timestamp, int, unix timestamp]
  [hashtags/mentions, array of strings]
  [link to image of user, url]
  [tweet text, string]
  [links included in tweet, array of urls]
  [how many times tweet favorited, int]
  [how many retweets does tweet have, int]

