import praw
from praw.models import MoreComments
from collections import Counter

reddit = praw.Reddit(client_id = "yWVZwG37_5pKcw", client_secret="Tep3GvoINonZ6YpDSMLRTtTeb3lhPQ", user_agent="Judescrape")
cmv = reddit.subreddit("changemyview")

def Top():
    """The 10 TOP Posts and it's comments' statistics"""
    Setentia = 0
    Polysyndenton = 0
    Anaphora = 0
    for post in cmv.top(limit = 10):
        print()
        print(post.title)
        # titles.append(post.title)
        submission = reddit.submission(id= post.id)
        for top_level_comment in submission.comments:
            comment_list = []
            and_list = []
            if isinstance(top_level_comment, MoreComments):
                continue
            x = list(top_level_comment.body.split(" "))
            brad = Counter(x)
            and_list.append(brad["and"])
            total_ands = sum(and_list)
            if total_ands > 1:
                Polysyndenton +=1
            if any(x.count(element) > 1 for element in x) == True:
                Anaphora +=1
                continue
            if "''" or '""' in x:
                Setentia +=1
                continue
            comment_list.append(x)
        print("Setentia: ", Setentia)
        print("Polysyndenton: ", Polysyndenton)
        print("Anaphora: ", Anaphora)
        Setentia = Setentia - Sententia
        Polysyndenton = Polysyndenton - Polysyndenton
        Anaphora = Anaphora - Anaphora
Top()
