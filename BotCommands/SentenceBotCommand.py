import os
import logging
import re
import random
from SlackBot.BotCommands.ABotCommand import ABotCommand
from SlackBot.BotCommands.ABotCommand import BotRole
from SlackBot.BotCommands.ABotCommand import BotResponse
from SlackBot.services import gsheet_queries as gsheet


class SentenceBotCommand (ABotCommand):

    def __init__(self, text=None):
        self.gsheet_id = None
        self.gsheet_tab_id = None
        self.bot_name = None
        self.bot_query = None

        if text is not None:
            m = re.search(r"--bot=(\w+)( .*)*", text)
            if m is not None:
                self.bot_name = m.group(1)
                if m.group(2) is not None:
                    self.bot_query = m.group(2)
                else:
                    self.bot_query = text

        ABotCommand.__init__(self, text)


    def execute(self, role: BotRole) -> BotResponse:
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info('sentence')
        print('sentence')

        self.apply_authorisations(role)

        br = BotResponse()

        if self.gsheet_id is None or self.gsheet_tab_id is None:
            br.text = "Sorry, I can't do that"
        else:
            res = ''
            parts = gsheet.query(self.gsheet_id, self.gsheet_tab_id + '!A1:A102', '')

            br.username = parts[0][0]
            br.icon_url = parts[1][0]


            partsCount = random.randint(2, 4)

            indexList = list()

            for i in range(partsCount):
                index = random.randint(2, len(parts) - 1)
                if index in indexList:
                    continue

                indexList.append(index)
                res += parts[index][0]
                if i < partsCount - 1:
                    res += ", "

            br.text = res

        return br


    def apply_authorisations(self,role):

        if role == BotRole.MANAGERS:
            self.gsheet_id = os.environ.get('GSHEET_SENTENCES_MGR_SPREADSHEET_ID', 'n/a')
            self.gsheet_tab_id = self.bot_name

        elif role == BotRole.DE:
            self.gsheet_id = os.environ.get('GSHEET_SENTENCES_DE_SPREADSHEET_ID', 'n/a')
            self.gsheet_tab_id = "kalenzabot"

        else:
            pass





