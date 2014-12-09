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
  [user twitter handle]
  [user name]
  [user twitter id]
  [is tweet in reply to another?]
  [does tweet have a parent?]
  [timestamp]
  [hashtags/mentions]
  [link to image of user]
  [tweet text]
  [links included in tweet]
  [how many times tweet favorited]
  [how many retweets does tweet have]

