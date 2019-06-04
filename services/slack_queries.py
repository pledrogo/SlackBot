import os
#import slack
from slackclient import SlackClient

def send(channel, text, username, icon_url):
    webhook_url = 'https://slack.com/api/chat.postMessage'
    token = os.environ.get('SLACK_MSG_TOKEN', 'N/A')
    sc = SlackClient(token)

    response = sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        as_user='false',
        username=username,
        icon_url=icon_url
    )

    return response['ok']