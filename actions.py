# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests 
import json
import tweepy
from tqdm import tqdm
import numpy as np
import json
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import teradatasql
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="aiquotient.json"

# class ActionHelloWorld(Action):
#     def name(self) -> Text:
#         return "action_hello_world"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Hello World!")
#         return []

class ActionQuestion(Action):
    def name(self) -> Text:
        return "action_question"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
       	dispatcher.utter_message(text="Which Machine Learning algorithm is good with outliers?")
        return []

class ActionMleStart(Action):
    def name(self) -> Text:
        return "action_mlestart"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        API_PREFIX = "http://10.25.44.225:30011/terabot/api/v1"
        API_ENDPOINT = API_PREFIX + "/start"
        # data to be sent to api 
        data = {} 
       	dispatcher.utter_message(text="Sure Thing!")
        #dispatcher.utter_message(text="Attempting to start MLE")
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data) 
        # while(True):
        #     data = {}
        #     API_ENDPOINT = API_PREFIX + "/status"
        #     r = requests.post(url = API_ENDPOINT, data = data)
        #     reply = json.loads(r.text)
        #     if(reply["status"] == True):
        #         break
        # extracting response text  
        # bot_reply = json.loads(r.text)
        dispatcher.utter_message(text="MLE is up")
        return []

# class ActionMleStop(Action):
#     def name(self) -> Text:
#         return "action_mlestop"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         API_PREFIX = "http://10.25.44.225:30011/terabot/api/v1"
#         API_ENDPOINT = API_PREFIX + "/stop"
#         # data to be sent to api 
#         data = {} 
#         dispatcher.utter_message(text="Attempting MLE Stop")
#         # sending post request and saving response as response object 
#         r = requests.delete(url = API_ENDPOINT, data = data) 
#         # extracting response text  
#         bot_reply = json.loads(r.text)
#         dispatcher.utter_message(text=bot_reply["message"])
#         return []

class ActionMleStatus(Action):
    def name(self) -> Text:
        return "action_mlestatus"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        API_ENDPOINT = "http://10.25.44.225:30011/terabot/api/v1/status"
        #dispatcher.utter_message(text="Im right on it!")
        # data to be sent to api 
        data = {} 
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data) 
        # extracting response text  
        bot_reply = json.loads(r.text)
        dispatcher.utter_message(text=bot_reply["message"])
        return []

class ActionTweet(Action):
    def name(self) -> Text:
        return "action_tweet"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        auth = tweepy.OAuthHandler('SpvZkd6MAEl7cYKqihxI9eX72','XO4LIBymaWT5TVMICP3iluh9muxzk2qAixYu2dVJiSrAzlleqv')
        auth.set_access_token('1105782144566288384-TAWiXN8cZ59fX2cSYPoUvuzg2QZ8wA',
                    'SRe0Wh7wfqtBaic89DbBQVPb0V2qo5aUgSBrI4zUSLsrr')
        api=tweepy.API(auth)
        username = 'saicharantej'
        con = teradatasql.connect('{"host":"sdt17023.labs.teradata.com", "user":"alice", "password":"alice"}')
        with con.cursor() as cur:
            rows = cur.execute("select dt1.text, dt1.created_at from ALICE.tweets as dt1, (select max(rt_cnt) as rt_cnt from ALICE.tweets)as dt2 where dt1.rt_cnt = dt2.rt_cnt;")
            reply = ""
            datec = ""
            for row in rows:
                reply = row[0]
                datec = row[1]
                break
        dispatcher.utter_message(text="Here's the tweet with max retweets, \""+reply+"\". Created on, "+datec+"!")
        return []

class ActionSentiment(Action):
    def name(self) -> Text:
        return "action_sent"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        client = language.LanguageServiceClient()
	    # [END language_python_migration_client]
	    

        #con = teradatasql.connect('{"host":"sdt17023.labs.teradata.com", "user":"alice", "password":"alice"}')
        #text = ""
        #with con.cursor() as cur:
        #    rows = cur.execute("select dt1.text, dt1.created_at from ALICE.tweets as dt1, (select max(fav_cnt) as fav_cnt from ALICE.tweets)as dt2 where dt1.fav_cnt = dt2.fav_cnt;")
        #    for row in rows:
        #        text = row[0]
        #        break
	    text = u'This is a really awful movie'
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

	    # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        print('Text: {}'.format(text))
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
        reply = ""
        if(sentiment.score > 0.0):
        	reply = "Positive"
        elif(sentiment.score < 0.0):
        	reply = "Negative"
        else:
        	reply = "Neutral"
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
        dispatcher.utter_message(text="With Google's TextAnalysis api, Sentiment on that tweet seems to be, "+reply+"!")
        dispatcher.utter_message(text="and just so you know, Teradata is soon launching NOS capabilities!")

        return []
