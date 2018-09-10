import os
import praw
import json
import webbrowser
import pprint

class Client():
    def __init__(self, username, password, user_agent, client_id, client_secret):
        self._username = username
        self._password = password
        self._user_agent = user_agent
        self._client_id = client_id
        self._client_secret = client_secret
        self._user = None
        self._reddit = None
        self._subreddit = []

    def loadReddit(self):
        self._reddit = praw.Reddit(user_agent=self._user_agent,
                                   username=self._username,
                                   password=self._password,
                                   client_id=self._client_id,
                                   client_secret=self._client_secret)
        self._reddit.store_json_result = True
        print("Read Only: " +  str(self._reddit.read_only))
        print(self._reddit)
        self._user = self._reddit.redditor(self._username)
        print(self._user)
        self._reddit.user.me()


    def openBrowser(self):
        url = self._reddit.get_authorize_url('uniqueKey', 'identity', True)
        webbrowser.open(url)

    def addSubReddits(self,subreddit):
        self._subreddit = self._reddit.subreddit(subreddit)

    def exportToJson(self, data, filepath, filename):
        try:
            with open((filepath + filename), 'w') as fp:
                json.dump(data, fp)
        except Exception as error:
            print("Unable to export dictionary as json")
            print(error)


    def getSubmissionAttributes(self,submissions):
        submission_att = {}

        for submission in submissions:
            attributes = vars(submission)
            pprint.pprint(attributes)
            submission_att[submission.title] = attributes
        return submission_att

    def getSubredditAttributes(self,subreddits):
        subreddit_att = {}
        for subreddit in subreddits:
            attributes = vars(subreddit)
            pprint.pprint(attributes)
            subreddit_att[subreddit.display_name] = attributes
        return subreddit_att

    def getRedditorAttributes(self,redditors):
        redditors_att = {}
        for redditor in redditors:
            attributes = vars(redditor)
            pprint.pprint(attributes)
            redditors_att[redditor.name] = attributes
        return redditors_att

    #def getRedditors(self):


    def getSubreddits(self, subreddit):
        subreddits = []
        for sub in subreddit:
            subreddits.append(self._reddit.subreddit(sub))
        return subreddits

    def getSubmissions(self, mode='hot', value=1, sub_url=None):
        """
        Return single or multiple submissions from a single subreddit
        """

        if sub_url:
            return self._reddit.submission(url=sub_url)

        new_submissions = []
        submissions = None
        if mode is 'hot':
            submissions = self._subreddit.hot(limit=value)
        elif mode is 'gilded':
            submissions = self._subreddit.gilded(limit=value)
        elif mode is 'controversial':
            submissions = self._subreddit.controversial(limit=value)
        elif mode is 'new':
            submissions = self._subreddit.new(limit=value)
        elif mode is 'rising':
            submissions = self._subreddit.rising(limit=value)
        elif mode is 'top':
            submissions = self._subreddit.top(limit=value)

        if value is 1:
            return submissions

        for submission in submissions:
            new_submissions.append(submission)
            #print(submission)
            print(submission.title)
            #print(submission.id)
            print(submission.url)
            #print(submission.comments)
            '''
            for comment in submission.comments:
                print(comment)
                print(comment.body)
            
            submission.title
            submission.score
            submission.id
            submission.url
            '''
        return new_submissions

    def testJson(self,submission):
        for comment in submission.comments:
            print(comment.body)


    def createCommentJson(self,comment):
        data = {}
        data['reply']
        if comment.replies is None:
            data['comment'] = None
        else:
            for reply in comment.replies:
                data['replies'].append(self.createCommentJson(reply))


        return data

    """
    Subreddit
        Thread
            Comment
                Comment
                    Comment
                Comment
                    Comment
            Comment
                Comment
            Comment
                Comment
                    Comment
                    Comment
                        Comment
        Thread
            Comment
                Comment
                    Comment
                Comment
                    Comment
            Comment
                Comment
            Comment
                Comment
                    Comment
                    Comment
                        Comment
    
    """


"""
JSON FORMAT
submission['title']
submission['id']
submission['author']
submission['text']
submission['comments']
comment['author']
comment['date']
comment['text']
comment['downvotes']
comment['upvotes']
comment['comments']
"""



