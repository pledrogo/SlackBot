import os
import logging

from BotCommands.ABotCommand import ABotCommand
from BotCommands.ABotCommand import BotRole
from BotCommands.BotResponse import BotResponse

class HelpBotCommand (ABotCommand):

    def execute(self, role: BotRole) -> BotResponse:
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info('help')
        print('help')

        text = self.get_text(role)
        return BotResponse(username='de-bot.helper', icon_url='', text=text)


    def get_text(self, role):
        text = ""

        if role == BotRole.DE:
            text = os.environ.get('HELP_DE_TEXT', 'n/a')

        elif role == BotRole.MANAGERS:
            text = os.environ.get('HELP_MGR_TEXT', 'n/a')

        else:
            text = os.environ.get('HELP_ALL_TEXT', 'n/a')

        return text
