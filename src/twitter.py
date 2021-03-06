import pytwitter
import time
import datetime
from mylib import unescape, myprint

  
def getTweet(user, n):
  now = int(time.time())
  t_logo = "0,10twitter"
  try:
    t_api = pytwitter.Api(consumer_key = 'laKcPz3kAAH3TVz8wIRAA',
                          consumer_secret = 'P7CD74v1ea5dO9JvJvv0blAmZaGmhQebAJIH2XLCI',
                          access_token_key = '1523563723-gcn8yyeFiGK1PlxfnoPve9j0QWO3OVP2qyfhTCs',
                          access_token_secret = 'QihKi7KCPFD7n9Yq3AFXDgWVc2vO3dmlzhClgsDxrU0')
    
    t_user = t_api.GetUser(None, user)._screen_name
    tweets = t_api.GetUserTimeline(screen_name = t_user, count = 200)
    
    if not tweets:
      return "%s User: %s has no tweets" % (t_logo, t_user)
      
    else:
      tweet = tweets[n].GetText()
      t = int(tweets[n].GetCreatedAtInSeconds())
      created = "Posted %s ago" % (datetime.timedelta(seconds=now-t))
      tweet = unescape(tweet).replace('\n', ' ')
      return "%s @%s: %s (%s)" % (t_logo, t_user, tweet, created)
      
  except pytwitter.TwitterError as e:
    myprint("TwitterError: %s" % (e))
    return "%s Error: Nope." % (t_logo)
  except IndexError:
    return "%s Error: You have gone too far (keep below 200)" % (t_logo)
