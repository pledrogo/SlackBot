import sys
sys.path.append('../')
from SlackBot.CommandRouter import CommandRouter
import pytest
from SlackBot.BotCommands.ABotCommand import ABotCommand
from SlackBot.BotCommands.ABotCommand import BotRole
from SlackBot.BotCommands.AdminBotCommand import AdminBotCommand
from SlackBot.BotCommands.HelpBotCommand import HelpBotCommand
from SlackBot.BotCommands.SupportBotCommand import SupportBotCommand
from SlackBot.BotCommands.SentenceBotCommand import SentenceBotCommand




def test_load_1():

    inputStr = "token=mytok3n&channel_id=DDJTB7XME&channel_name=directmessage&user_id=UBE8HRL6A&user_name=patrick.ledrogo&command=%2Fkalenzabot&text=support&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT027K0ZC9%2F470887661185%2FT299DJrz5rvn7VojCRry8Gie&trigger_id=471692823445.2257033417.52ea5aed2846b7466f2f2aef1df31e7d"
    cr = CommandRouter(inputStr)

    assert cr.token == "mytok3n"
    assert cr.channel == "DDJTB7XME"
    assert cr.user_id == "UBE8HRL6A"
    assert cr.user_name == "patrick.ledrogo"
    assert cr.command == "/kalenzabot"
    assert cr.text == "support"

def test_route_1():

    cr = CommandRouter()

    cr.token == "mytok3n"
    cr.channel = "DDJTB7XME"
    cr.user_id = "UBE8HRL6A"
    cr.user_name = "patrick.ledrogo"
    cr.command = "/kalenzabot"
    cr.text = "support"

    bc = cr.route_command()

    assert type(bc) is SupportBotCommand






