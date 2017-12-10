import requests, sys, tweepy, time, string, random

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

STATUSES = (
    "#ProBowlVote @DangeRussWilson @TDLockett12 @prichiejr @TheJimmyGraham @JustinBritt68 @DuaneBrown76 @DougBaldwinJr",
    "#ProBowlVote @Earl_Thomas @TheRealFrankC_ @mosesbread72 @SdotRich91 @Bwagz54 @KJ_WRIGHT34",
    "Pro Bowl voting is #EZZZ, just hit that RT button! 1️⃣ RT = 1️⃣ special teams #ProBowlVote 🙌 @Neiko15 @jonryan9 @BlairWalsh3 @Ottomatic82 @D_alexander57",
    "#ProBowlVote (RTs count!) @DangeRussWilson @TDLockett12 @prichiejr @TheJimmyGraham @JustinBritt68 @DuaneBrown76 @DougBaldwinJr",
    "#ProBowlVote (RTs count!) @Earl_Thomas @TheRealFrankC_ @mosesbread72 @SdotRich91 @Bwagz54 @KJ_WRIGHT34",
    "@Bwagz54 deserves Defensive Player of the Year #ProBowlVote",
    "@DangeRussWilson deserves league MVP #ProBowlVote",
    "#ProBowlVote (RTs count!) @Earl_Thomas @TheRealFrankC_ @mosesbread72 @SdotRich91 @Bwagz54 @KJ_WRIGHT34",
    "#ProBowlVote (RTs count!) @DangeRussWilson @TDLockett12 @prichiejr @TheJimmyGraham @JustinBritt68 @DuaneBrown76 @DougBaldwinJr",
    "☝️ RT = ☝️ #ProBowlVote vote Let's help @KJ_WRIGHT34 earn consecutive Pro Bowl honors!",
    " 1️⃣ RT = 1️⃣ #ProBowlVote for @TheJimmyGraham!",
    "We know he's got your vote for #DPOY. How 'bout a 4th consecutive Pro Bowl honor? 🏆 Each RT counts as  1️⃣ @BWagz54 #ProBowlVote!",
    "Tied for the @NFL lead in TDs, Jimmy Graham is at the top of his game. ￼ RT to #ProBowlVote @TheJimmyGraham 🛩",
    "RT to #ProBowlVote @mosesbread72!",
    "Retweet any of my tweets to vote Seahawks players to the Pro Bowl!"
)

def make_unique():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))

while True:
    for status in STATUSES:
        next_status = status + " " + make_unique()
        print(next_status)
        api.update_status(next_status)
        print("Sleeping...")
        time.sleep(60)