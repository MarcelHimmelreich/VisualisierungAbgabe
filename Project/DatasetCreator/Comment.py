
import praw
import json

class Comment():
    def __init__(self, comment):
        self.author = comment.author
        self.id = comment.id
        self.url = comment.permalink
        self.content = comment.body
        self.score = comment.score
        self.likes = comment.likes

        self.upvote = comment.ups
        self.downvote = comment.downs
        self.comment = comment

    def getJson(self):
        return self.getResponse()

    def getResponse(self):
        '''Recursive Function to get Comment Forest'''
        comment = {}
        comment['author'] = str(self.author)
        comment['id'] = self.id
        comment['url'] = str(self.url)
        comment['content'] = self.content
        comment['score'] = int(self.score)
        if self.likes is None:
            comment['likes'] = 0
        else:
            comment['likes'] = self.likes
        comment['upvote'] = int(self.upvote)
        comment['downvote'] = int(self.downvote)
        comment['comments'] = []
        if self.comment.replies:
            for reply in self.comment.replies:
                if isinstance(reply, praw.models.Comment):
                    new_comment = Comment(reply)
                    comment['comments'].append(new_comment.getResponse())
        else:
            comment['comments'] = 0
        return comment
