from twython import Twython,TwythonError
import configparser
                                                                                        #config lib , logging to log all the operations , try except blocks

class twitterthon:
    def __init__(self):

        config = configparser.ConfigParser()
        config.read('keys.txt')
        APP_KEY = config.get('key','APP_KEY')
        APP_SECRET = config.get('key','APP_SECRET')
        twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        self.twitter = Twython(APP_KEY,APP_SECRET,access_token = ACCESS_TOKEN)

    def followers(self,screen_name):
       followers = []

       try:
           followers_data = self.twitter.get_followers_list(screen_name=screen_name)
           followers = [each['screen_name'] for each in followers_data['users']]

        except TwythonError as error:
           print error

        return followers

    def tweets_list(self,screen_name):
        tweets=[]
        try:
            result = self.twitter.get_user_timeline(screen_name=screen_name)
            tweets = [i['text'] for i in result]

        except TwythonError as error:
            print error

        return tweets

    def search_tweets(self, screen_name, search_text):
        search_tweet_result = []
        try:
            result = self.twitter.get_user_timeline(screen_name=screen_name)
            search_tweet_result = [i['text'] for i in result if search_text in i['text']]

        except TwythonError as error:
            print error

        return search_tweet_result

    def gettingsimilarUser(self):
        similar_users = []
        try:
            user1 = self.twitter.get_followers_ids(screen_name=user_1)
            user2 = self.twitter.get_followers_ids(screen_name=user_2)
            user1_followers = [i['screen_name'] for i in user1['users']]
            user2_followers = [i['screen_name'] for i in user2['users']]
            for i in user1_followers:
                for j in user2_followers:
                    data1 = self.twitter.show_user(user=i)
                    data2 = self.twitter.show_user(user=j)
                if data1 ==data2:
                    print(data1["screen_name"])

        except TwythonError as error:
            print error

        return similar_users


t = twitterthon()
t.followers()
t.searching_tweet()
t.gettingsimilarUser()
