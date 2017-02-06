from twython import Twython


class twitterthon:
    def __init__(self):

        APP_KEY = '37Dc2q5kcUBhaAKtHaRo6zgtF'
        APP_SECRET = 'PWL1zNmJLSUaL2qGzCW2UzGSMAcReQ2v5WCY40swaamk2oHklb'
        twitter = Twython(APP_KEY, APP_SECRET,oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        self.twitter = Twython(APP_KEY,access_token= ACCESS_TOKEN)

    def followers(self):
        user=raw_input("Please enter a twitter name:")

        output = self.twitter.get_followers_list(screen_name=user)
        for each in output['users']:
            print each['screen_name']

    def searching_tweet(self):
        user = raw_input("Please enter a string to search tweets :")
        output = self.twitter.search(q=user)
        print output
        for tweet in output['statuses']:
            print tweet['text']

    def gettingsimilarUser(self):
        user1 = raw_input("Please enter a valid twitter screen name1:")
        output1 = self.twitter.get_followers_ids(screen_name=user1)
        user2 = raw_input("Please enter another valid twitter screen name2:")
        output2 = self.twitter.get_followers_ids(screen_name=user2)
        for i in output1["ids"]:
            for j in output2["ids"]:
                data1 = self.twitter.show_user(user=i)
                data2 = self.twitter.show_user(user=j)
                if data1 ==data2:
                    print(data1["screen_name"])


t = twitterthon()
t.followers()
t.searching_tweet()
t.gettingsimilarUser()
