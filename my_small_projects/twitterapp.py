from twython import Twython
from flask import Flask,render_template,request
import configparser
import logging

app = Flask(__name__)                               #config lib , logging to log all the operations , try except blocks

logging.basicConfig(filename='config_test.log',level=logging.DEBUG)


config = configparser.ConfigParser()
config.read('config_keys.ini')
APP_KEY = config.get('keys','APP_KEY')
APP_SECRET = config.get('keys','APP_SECRET')

twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY,APP_SECRET,access_token = ACCESS_TOKEN)

@app.route('/')
def index():
    return render_template('twitterthon.html')

@app.route('/followers')
def func1():
    return render_template('followers_list.html')



def followers(self,screen_name):    #This function returns the followers present for the given name
    followers = []

    try:
        followers_data = self.twitter.get_followers_list(screen_name=screen_name)
        followers = [each['screen_name'] for each in followers_data['users']]

    except Exception, e:
        logging.info('error in the followers function',str(e))

    return followers

def tweets_list(self,screen_name):          #returns the tweets done by user
    tweets=[]
    try:
        result = self.twitter.get_user_timeline(screen_name=screen_name)
        tweets = [i['text'] for i in result]

    except Exception, e:
            logging.info('there is an error in the tweets_list function',str(e))

    return tweets

def search_tweets(self, screen_name, search_text):          #This function searches the tweets by given string
    search_tweet_result = []
    try:
        result = self.twitter.get_user_timeline(screen_name=screen_name)
        search_tweet_result = [i['text'] for i in result if search_text in i['text']]

    except Exception, e:
        logging.info('error present in the search_tweets function',str(e))

    return search_tweet_result

def gettingsimilarUser(self,user1,user2):           #Helps to find the similar users by comparing them

    similar_users = []
    try:
        user_1 = self.twitter.get_followers_ids(screen_name=user1)
        user_2 = self.twitter.get_followers_ids(screen_name=user2)
        user1_followers = [i['screen_name'] for i in user_1['users']]
        user2_followers = [i['screen_name'] for i in user_2['users']]
        for follower in user1_followers:
            if follower in user2_followers:
                similar_users.append(follower)

    except Exception, e:
        logging.info('error in getting similar users',str(e))

    return similar_users

if __name__ == '__main__':
    app.run()

#t = twitterthon()
#t.followers()
#t.searching_tweet()
#t.gettingsimilarUser()
