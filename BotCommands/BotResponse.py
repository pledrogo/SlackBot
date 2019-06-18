import os
import logging
from services import slack_queries as slack

class BotResponse:

    def __init__(self, username=None, icon_url=None, text=None):

        self.username = username
        self.icon_url = icon_url
        self.text = text


    def send(self, channel):
        async_msg = slack.send(channel, self.text, self.username, self.icon_url)

        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info("async status:{}".format(async_msg))

        return async_msg

