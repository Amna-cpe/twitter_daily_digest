import tweepy
import requests
import os
from os import environ
import time
import schedule
import io
import sys

API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKENY']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def create_twitter_digest():

    # Add the user Id you want to get tweets
    user_id = "JavaScriptKicks"

    # Add the number of tweets you want to get
    number_of_tweets = 10

    # count: maximum allowed tweets count
    # tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.

    timeline = api.user_timeline(
        screen_name=user_id, count=number_of_tweets, tweet_mode="extended")

    # Iterate and add to array of tweets
    arr = []
    for tweet in timeline:
        obj = {
            "img": tweet.user.profile_image_url,
            'username': tweet.user.screen_name,
            'name': tweet.user.name,
            'text': tweet.full_text,
            'createdAt': tweet.created_at,
            "link": "https://twitter.com/twitter/statuses/"+str(tweet.id)

        }
        arr.append(obj)

    # prepare the html page

    htmlDoc = """<!DOCTYPE html><html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Document</title>
        <style>
            body {
                background-color: rgb(233, 227, 227);
            }

            .tweet {
                margin: 20px auto;
                background-color: rgb(30, 28, 34);
                border: rgb(135, 135, 138) solid 1px;
                border-radius: 15px;
                padding: 30px;
                color: white;
            }

            .head {
                display: flex;
                justify-content: flex-start;
            }

            .head img {
                height: 50px;
                width: 50px;
                border-radius: 50%;
                object-fit: cover;
            }

            .user {
                margin-left: 10px;
                display: flex;
                flex-direction: column;
            }

            .user small {
                color: #c0c0c0c0;
            }

            .tweet-content {
                padding: 10px;
                width: 70%;
                margin-left: 50px;
            }

            .time {
                color: #c0c0c0c0;
                margin-left: 50px;
            }
        </style>
    </head>

    <body>
        <h1 style="text-align: center;">Your favourite twitter acc. daily digest</h1>
    """

    # now append to the html page the tweets
    for tweet in arr:
        htmlDoc += f""" <div class="tweet"><div class="head">
                <img src={tweet['img']} alt='head'>
                <div class="user">
                    <strong>{tweet['name']}</strong>
                    <small>{tweet['username']}</small>
                </div>
            </div>
    
            <div class="tweet-content">
                    {tweet['text']}
                <a href={tweet['link']} target="_blank">tweet</a>
            </div>

            <div class="time">
                <small> {tweet['createdAt']}</small>
            </div>
        </div>
        """

    htmlDoc += """<footer style="text-align: center;"> <strong >Github:Amna-cpe</strong></footer>
        </body></html></body></html>"""

    # save the html page
    with io.open("test.html", "w", encoding="utf-8") as f:
        f.write(htmlDoc)
