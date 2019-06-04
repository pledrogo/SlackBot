import os
import logging
import random
import re
from datetime import date
from services import gsheet_queries as gsheet


def kalenzabot(role, text):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('text ={}'.format(text))
    print(text)

    bot = dict(username='', icon_url='', text=text + ": command not found")

    if role in 'manager':
        if 'support' in text:
            bot = query_support(text)
        elif '--admin' in text:
            bot = dict(username='', icon_url='',
                             text = os.environ.get('GSHEET_MGR_LINK','n/a'))
        elif '--help' in text:
            bot = dict(username='', icon_url='',
                             text= os.environ.get('HELP_MGR_TEXT','n/a'))
        else:
            gsheetid = os.environ.get('GSHEET_SENTENCES_MGR_SPREADSHEET_ID','n/a')
            m = re.search(r"--bot=(\w+)( .*)*", text)
            if m is not None:
                query = text
                botname = m.group(1)
                if m.group(2) is not None:
                    query = m.group(2)
                bot = query_sentences(gsheetid, botname, query)
            else:
                bot = dict(username='', icon_url='', text=text + ": didnt get it...")

    elif role in 'de':
        if 'support' in text:
            bot = query_support(text)
        elif '--help' in text:
            bot = dict(username='', icon_url='',
                       text=os.environ.get('HELP_MGR_TEXT', 'n/a'))
        elif 'kalenzadmin' in text:
            bot = dict(username='', icon_url='',
                             text=os.environ.get('GSHEET_MGR_LINK','n/a'))
        else:
            gsheetid = os.environ.get('GSHEET_SENTENCES_DE_SPREADSHEET_ID','n/a')
            bot = query_sentences(gsheetid, "kalenzabot", text)
    else:
        bot = query_support(text)

    return bot



def query_support(text):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    bot = dict(username='patrick.ledrogo', icon_url='https://ca.slack-edge.com/T027K0ZC9-UBE8HRL6A-6e077c11439c-72',
               text='')

    gsheetid = os.environ.get('GSHEET_SUPPORT_SPREADSHEET_ID','N/A')
    gsheetrange = os.environ.get('GSHEET_SUPPORT_RANGE_NAME','N/A')

    support = gsheet.query(gsheetid, gsheetrange, '')
    res = ""
    weekNumber = date.today().isocalendar()[1]
    thisweek = "Cette semaine"
    if 'semaine prochaine' in text or 'next week' in text:
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
        batman = "...personne et c'est *pas normal*..."
    if not robin:
        robin = "...a sorti son JOKER"

    bot['text'] = os.environ.get('SUPPORT_FORMAT_TXT','n/a').format(thisweek, batman, robin)

    return bot


def query_sentences(gsheetid, tabid, text):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    bot = dict(username='kalenzabot', icon_url='', text='')

    # a supprimer pour mettre du filtering
    text = ''
    ###

    res = ''
    parts = gsheet.query(gsheetid, tabid + '!A1:A102', '')

    bot['username'] = parts[0][0]
    bot['icon_url'] = parts[1][0]
    if text == '':
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
    else:
        resList = filter(lambda x: (x.find(text) > 0), parts)

    bot['text'] = res

    return bot