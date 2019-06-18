import os
import logging
from BotCommands.ABotCommand import ABotCommand
from BotCommands.ABotCommand import BotRole
from BotCommands.BotResponse import BotResponse

class AdminBotCommand(ABotCommand):


    def execute(self, role: BotRole) -> BotResponse:
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info('admin')
        print('admin')

        text = self.get_text(role)
        return BotResponse(username='de-bot.admin', icon_url='', text=text)


    def get_text(self, role):

        text = ""

        if role == BotRole.DE:
            text = os.environ.get('GSHEET_DE_LINK', 'n/a')

        elif role == BotRole.MANAGERS:
            text = os.environ.get('GSHEET_MGR_LINK', 'n/a')

        else:
            text = "Sorry but no. I can't trust you"

        return text
