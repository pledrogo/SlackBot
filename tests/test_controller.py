import sys
sys.path.append('../')
from SlackBot.BotCommands.ABotCommand import ABotCommand
from SlackBot.BotCommands.ABotCommand import BotRole

from SlackBot.BotCommands.AdminBotCommand import AdminBotCommand
from SlackBot.BotCommands.HelpBotCommand import HelpBotCommand
from SlackBot.BotCommands.SupportBotCommand import SupportBotCommand
from SlackBot.BotCommands.SentenceBotCommand import SentenceBotCommand
from SlackBot.security import auth_by_token
import os

from SlackBot import controller as module



def test_kalenzabot_admin_1():

    bc = AdminBotCommand()
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "DDJTB7XME" # direct message

    assert module.kalenzabot(bc) is None

def test_kalenzabot_support_1():

    bc = SupportBotCommand()
    bc.text = "support"
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GE9EENXSP" # kalenzatestde

    assert module.kalenzabot(bc) is None

def test_kalenzabot_support_2():
    bc = SupportBotCommand()
    bc.text = "support next week"
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GDZRVNS8Y"  # kalenzatestmgr

    assert module.kalenzabot(bc) is None

def test_kalenzabot_sentence_1():
    bc = SentenceBotCommand()
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GDZRVNS8Y"  # kalenzatestmgr

    assert module.kalenzabot(bc) is None

def test_kalenzabot_sentence_2():
    bc = SentenceBotCommand()
    bc.text = "--bot=martinbot"
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GDZRVNS8Y"  # kalenzatestmgr

    assert module.kalenzabot(bc) is None


def test_de_support():
    bc = SupportBotCommand()
    bc.text = "support next week"
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GKL53UX6Y" # kalenzabotall

    assert "batman" in module.de(bc)

def test_de_other():
    bc = SentenceBotCommand()
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    bc.channel = "GKL53UX6Y" # kalenzabotall

    assert "Sorry" in module.de(bc)

@auth_by_token
def sample_fonction(botCommand):
    return botCommand.token

def test_auth():
    bc = ABotCommand()
    bc.token = os.environ.get('SLACK_REQUEST_TOKEN', 'N/A')
    assert sample_fonction(bc) == bc.token


