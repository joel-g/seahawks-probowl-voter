import requests, sys, tweepy, time, string, random
from random import randint

config = open('config.ini','r')
tokens = config.readlines()
config.close()

CONSUMER_KEY = tokens[0].rstrip()
CONSUMER_SECRET = tokens[1].rstrip()
ACCESS_KEY = tokens[2].rstrip()
ACCESS_SECRET = tokens[3].rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

PLAYERS = (
    "@DangeRussWilson", "@TDLockett12", "@DuaneBrown76", "@DougBaldwinJr", "@Earl_Thomas",
    "@TheRealFrankC_", "@Bwagz54", "@KJ_WRIGHT34", 
    "@DougBaldwinJr", "@BabyLead", "@ShaquillG", "@Shaquemgriffin", "@LWillson_82", "#JustinBritt", "#JRSweezy", "@DJTheWarrior76", "@GermainX1", "@ccarson_32", "@mdcksn", "@N_Vannett81", "@keke_mingo", "#davidmoore","@nuevexted", "@1j_reed"
    )

STATUSES = (
    "#ProBowlVote @DangeRussWilson @TDLockett12 #JustinBritt @DuaneBrown76 @DougBaldwinJr",
    "#ProBowlVote @TheRealFrankC_ @Bwagz54 @KJ_WRIGHT34",
    "Pro Bowl voting is #EZZZ, just hit that RT button! 1️⃣ RT = 1️⃣ special teams #ProBowlVote 🙌",
    "Keep voting @Seahawks #ProBowlVote @DangeRussWilson @DougBaldwinJr @TheRealFrankC_ @TDLockett12 @ShaquillG @BabyLead @Bwagz @mdcksn @DuaneBrown76 #JustinBritt @1j_reed @DJTheWarrior76",
    "🚨 Pro Bowl social voting is LIVE! 🚨 1️⃣ retweet = 1️⃣ #ProBowlVote for @DangeRussWilson!",
    "RT to #ProBowlVote!",
    "Retweet any of my tweets to vote Seahawks players to the Pro Bowl!",
    "RT to send our @Seahawks to the #ProBowlVote! #Seahawks @DangeRussWilson @BabyLead @ShaquillG @Shaquemgriffin @TDLockett12 @Bwagz @TheRealFrankC_"
    )



def make_unique():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))

def random_sleep():
    sleep_time = randint(300, 600)
    print("Sleeping for " + str(sleep_time) + " seconds.")
    time.sleep(sleep_time)

while True:
    custom_status = "Retweet to #ProBowlVote " + random.choice(PLAYERS) + " " + random.choice(PLAYERS) + " " + random.choice(PLAYERS) + " " + random.choice(PLAYERS) + " " + make_unique() + " #Seahawks"
    print(custom_status)
    api.update_status(custom_status)
    random_sleep()
    next_status = random.choice(STATUSES) + " " + make_unique()
    print(next_status)
    api.update_status(next_status)
    random_sleep()
    
