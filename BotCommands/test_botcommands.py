import pytest


from ABotCommand import ABotCommand
from ABotCommand import BotRole
from AdminBotCommand import AdminBotCommand
from HelpBotCommand import HelpBotCommand
from SupportBotCommand import SupportBotCommand
from SentenceBotCommand import SentenceBotCommand



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
