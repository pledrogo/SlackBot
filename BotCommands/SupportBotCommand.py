import os
import logging
from datetime import date
from BotCommands.ABotCommand import ABotCommand
from BotCommands.ABotCommand import BotRole
from BotCommands.BotResponse import BotResponse
from services import gsheet_queries as gsheet

class SupportBotCommand (ABotCommand):


    def execute(self, role: BotRole) -> BotResponse:
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        gsheetid = os.environ.get('GSHEET_SUPPORT_SPREADSHEET_ID', 'N/A')
        gsheetrange = os.environ.get('GSHEET_SUPPORT_RANGE_NAME', 'N/A')

        br = BotResponse()
        br.username = 'patrick.ledrogo'
        br.icon_url = 'https://ca.slack-edge.com/T027K0ZC9-UBE8HRL6A-6e077c11439c-72'

        support = gsheet.query(gsheetid, gsheetrange, '')

        res = ""
        weekNumber = date.today().isocalendar()[1]
        thisweek = "Cette semaine"

        if 'semaine prochaine' in self.text or 'next week' in self.text:
            weekNumber = weekNumber + 1
            thisweek = "La semaine prochaine"
        weekColIndex = 0
        batman = None
        robin = None

        # logger.info('row {} col {} val {} '.format(5,10,support[5][10]))

        for i in range(len(support[0]) - 1):
            # logger.info('support weeks {}'.format(support[0][i]))
            # logger.info(' week= {}'.format(weekNumber))
            if support[0][i] == str(weekNumber):
                weekColIndex = i
                # logger.info('support week found {}'.format(support[0][i]))
                break
        # logger.info('support length {}'.format(len(support)))

        for j in range(len(support) - 1):
            # logger.info(j)
            # logger.info('row {} col {} val {} '.format(j,weekColIndex,support[j][weekColIndex]))
            if support[j][weekColIndex] == 'SUP':
                batman = support[j][1]
                # logger.info('batman found {}'.format(support[j][1]))
            elif support[j][weekColIndex] == 'RUN':
                robin = support[j][1]
                # logger.info('robin found {}'.format(support[j][1]))
            if robin and batman:
                break
        if not batman:
            batman = "...personne et c'est *pas normal* @patrick.ledrogo !"
        if not robin:
            robin = "...a sorti son :black_joker: "

        br.text = os.environ.get('SUPPORT_FORMAT_TXT', 'n/a').format(thisweek, batman, robin)

        return br
