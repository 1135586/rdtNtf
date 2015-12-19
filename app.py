import praw
from pgi.repository import Notify
import time

#make praw object
r = praw.Reddit(user_agent='redditNotify')

#getting first 5 posts
#sumissions is generator object
submissions = r.get_subreddit('learnprogramming').get_hot(limit=2)

#make array of all tuple subreddits url and titile

data = []

Notify.init("init")

for it in submissions:
    #print(it.title)
    #print(it.url)
    data.append((str(it.title), str(it.score)))

titles = ''

for i in data:
    titles +="\n" +  i[0] + "\n"+ " score: " + i[1] + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"

name = "Reddit learnproramming: "+ "\n"
#
#print(data[0])
n = Notify.Notification.new(name, titles, "")
n.show()


