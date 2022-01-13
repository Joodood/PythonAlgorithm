import praw
import datetime

reddit = praw.Reddit(client_id = "yWVZwG37_5pKcw", client_secret="Tep3GvoINonZ6YpDSMLRTtTeb3lhPQ", user_agent="Judescrape")

class Scraper:
    def __init__(self, sub, sort = "top", lim=10, mode = 'w'):
        self.sub = sub
        self.sort = sort
        self.lim = lim
        self.mode = mode

    def set_sort(self):
        if self.sort == 'new':
            print("This is a 'new' object")
            return reddit.subreddit(self.sub).new(limit=self.lim)

        elif self.sort == 'top':
            print("This is a 'top' object")
            return reddit.subreddit(self.sub).top(limit = self.lim)

        elif self.sort == 'hot':
            print("This is a 'hot' object")
            return reddit.subreddit(self.sub).hot(limit = self.lim)
        else:
            self.sort = 'top'
            print("sort method was not recognized, going to default to top.")
            return self.sort

    def set_words():
        pass


if __name__ == '__main__':
    College = Scraper('College', lim = 100, mode = 'w', sort = 'top').set_sort()
    print(College)
