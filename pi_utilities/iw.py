from slack_helper import slack_notify_message
import time


IW_CHANNEL = 'C0ZBDJK7V'


def _slack(message):
    slack_notify_message(message=message, channel_id=IW_CHANNEL)


def get_new_tweets():
    return []


def printer_print(message):
    _slack(message)


def iw():
    while True:
        _slack('++ looking for new tweets')
        tweets = get_new_tweets()
        for tweet in tweets:
            printer_print(tweet)
        time.sleep(1)