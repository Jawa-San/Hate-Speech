import praw

reddit = praw.Reddit(
        client_id="T38IvvnBfiZjufqt4rIMiA",
        client_secret="11S6y8H5FFl-A7rBd1oPS5iu03KZmw",
        user_agent="Joe",
    )

all = reddit.subreddit('all')
f = open('entries.txt', 'a')
for t in all.search('Kanye', limit=5):
    f.write(t.url + '\n')
    f.write(t.title + '\n')
f.close()
