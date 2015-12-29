import praw
import urllib
import os


USER_AGENT = "imgur downloader test" #change to something unique
REDDIT = praw.Reddit(user_agent=USER_AGENT)
USER_SUBREDDITS = [] #add whatever subreddits you want images from ex: ["Wallpaper", "pics"]
MIN_SCORE = 300 #any submission below this value will be ignored
POSTS = {}
FOLDER_LOCATION = "/Where/You/Want/Images/To/Go"


def printList():
    print("Your subreddit list contains: ")
    for i in USER_SUBREDDITS:
        print(str(i))
    print("-------------")


def checkIfValidSubreddit():
    for i in USER_SUBREDDITS:
        sub = str(i)
        try:
            REDDIT.get_subreddit(sub, fetch=True)
        except praw.errors.NotFound:
            print("You have entered an invalid subreddit in your list. It has been removed.")
            removeSubreddit(sub)


def removeSubreddit(input):
    try:
        USER_SUBREDDITS.remove(input)
    except ValueError:
        pass


def getValidPosts():
    for i in USER_SUBREDDITS:
        subreddit = REDDIT.get_subreddit(str(i)).get_hot(limit=25)
        # subreddit = REDDIT.get_subreddit(str(i)).get_controversial(limit=25)
        # subreddit = REDDIT.get_subreddit(str(i)).get_new(limit=25)
        # subreddit = REDDIT.get_subreddit(str(i)).get_top(limit=25)
        # subreddit = REDDIT.get_subreddit(str(i)).get_rising(limit=25)
        for post in subreddit:
            if post.score >= MIN_SCORE and "imgur.com" in post.url:
                print("This post will be looked at.")
                POSTS[post.title] = post.url
            else:
                print("This post will not be looked at due to either: non-imgur url or did not meet minimum score requirement")


def downloadFromURL():
    if not os.path.exists(FOLDER_LOCATION):
        os.makedirs(FOLDER_LOCATION)
    os.chdir(FOLDER_LOCATION)
    for title, url in POSTS.items():
        path = os.path.join(FOLDER_LOCATION, title + ".jpg")
        #Start downloading
        if os.path.isfile(path):
            print("Skipped. This file already exists")
        else:
            try:
                urllib.request.urlretrieve(url, path)
            except:
                print("Download failed.")


if __name__ == '__main__':
    checkIfValidSubreddit()
    printList()
    getValidPosts()
    downloadFromURL()
