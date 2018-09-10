import Comment
import praw

class Submission():
    def __init__(self, submission):
        self.author = submission.author
        self.title = submission.title
        self.id =  submission.id
        self.url = submission.url
        self.viewcount = submission.view_count
        self.content = submission.selftext
        self.upvote = submission.ups
        self.downvote = submission.downs
        self.upratio = submission.upvote_ratio
        self.subreddit = submission.subreddit_name_prefixed
        self.comments = submission.comments

    def getJson(self):
        submission = {}
        submission['author'] = str(self.author)
        submission['id'] = self.id
        submission['title'] = str(self.title)
        submission['url'] = str(self.url)
        submission['content'] = str(self.content)
        submission['upvote'] = int(self.upvote)
        submission['downvote'] = int(self.downvote)
        submission['upratio'] = float(self.upratio)
        submission['subreddit'] = str(self.subreddit)
        submission['comments'] = self.getComments()
        return submission

    def getComments(self):
        comments = []
        for comment in self.comments:
            if isinstance(comment, praw.models.Comment):
                new_comment = Comment.Comment(comment)
                comments.append(new_comment.getJson())
        return comments