import sys
sys.path.append('../')
import pytest

from SlackBot.BotCommands.ABotCommand import ABotCommand
from SlackBot.BotCommands.ABotCommand import BotRole
from SlackBot.BotCommands.AdminBotCommand import AdminBotCommand
from SlackBot.BotCommands.HelpBotCommand import HelpBotCommand
from SlackBot.BotCommands.SupportBotCommand import SupportBotCommand
from SlackBot.BotCommands.SentenceBotCommand import SentenceBotCommand



def test_abotcommand_1():

    bc = ABotCommand("hello")
    br = bc.execute(BotRole.ALL)
    assert br.text == "hello"

def test_admincommand_1():

    bc = AdminBotCommand()
    br = bc.execute(BotRole.ALL)
    assert "Sorry" in br.text


def test_helpcommand_1():

    bc = HelpBotCommand()
    br = bc.execute(BotRole.DE)
    assert "support" in br.text

def test_sentencecommand_1():

    bc = SentenceBotCommand("--bot=martinbot")
    br = bc.execute(BotRole.MANAGERS)
    assert br.username == "Martin"

def test_sentencecommand_2():

    bc = SentenceBotCommand()
    br = bc.execute(BotRole.DE)
    assert br.username == "christophe.kalenzabot"