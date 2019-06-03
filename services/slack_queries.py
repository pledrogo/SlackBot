import os
import slack

def send(channel, text, username, icon_url):
    webhook_url = 'https://slack.com/api/chat.postMessage'
    token = os.environ.get('SLACK_MSG_TOKEN','N/A')
    client = slack.WebClient(token=token)


    response = client.chat_postMessage(
        channel=channel,
        text=text,
        as_user='false',
        username=username,
        icon_url=icon_url,

    )

    return response['ok']