import DataClient
import Submission
from pprint import pprint

subreddits = ["gaming", "AskReddit", "ProgrammerHumor", "Showerthoughts", "technology", "pcmasterrace", "StarWars", "Jokes", "MachineLearning"]
dictionary = {}
filepath = "E:/RedditDaten/"
client = DataClient.Client(username="KirbyDataBot",
                           password="bauhausvis",
                           user_agent="Data Streamer for Reddit Content ver 0.0a /u/KirbyDataBot",
                           client_id="x396BlWKhK3VTg",
                           client_secret="bwBi_xVKb8df_8MI3FxZLVEzNq8")
client.loadReddit()


for subreddit in subreddits:
    client.addSubReddits(subreddit)
    dictionary['submission'] = []
    for submission in client.getSubmissions(value=5):
        new_submission = Submission.Submission(submission)
        dictionary['submission'].append(new_submission.getJson())
    client.exportToJson(dictionary, filepath, subreddit+".json")