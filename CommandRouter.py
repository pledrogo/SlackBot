import logging
from urllib.parse import parse_qs

from BotCommands.AdminBotCommand import AdminBotCommand
from BotCommands.HelpBotCommand import HelpBotCommand
from BotCommands.SupportBotCommand import SupportBotCommand
from BotCommands.SentenceBotCommand import SentenceBotCommand

class CommandRouter:

    def __init__(self, input_str=None):
        self.text = ""
        self.token = ""
        self.channel = ""
        self.user_id = ""
        self.user_name = ""
        self.command = ""

        if input_str is not None:
            self.load(input_str)

    def load(self, input_str):

        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("body:{}".format(input_str))
        print("body:{}".format(input_str))

        payload = parse_qs(input_str)
        logger.info("payload:{}".format(payload))

        print(payload.keys())
        if 'text' in payload.keys():
            self.text = payload['text'][0]
        if 'token' in payload.keys():
            self.token = payload['token'][0]
        if 'channel_id' in payload.keys():
            self.channel = payload['channel_id'][0]
        if 'user_id' in payload.keys():
            self.user_id = payload['user_id'][0]
        if 'user_name' in payload.keys():
            self.user_name = payload['user_name'][0]
        if 'command' in payload.keys():
            self.command = payload['command'][0]

    def route_command(self):

        pc = None

        if 'support' in self.text:
            pc = SupportBotCommand(self.text)
        elif '--admin' in self.text or 'kalenzadmin' in self.text:
            pc = AdminBotCommand()
        elif '--help' in self.text:
            pc = HelpBotCommand()
        else:
            pc = SentenceBotCommand(self.text)


        pc.token = self.token
        pc.channel = self.channel

        return pc
