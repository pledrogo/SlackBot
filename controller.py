import logging

from SlackBot.BotCommands.ABotCommand import ABotCommand
from SlackBot.BotCommands.ABotCommand import BotRole
from SlackBot.security import get_role
from SlackBot.security import auth_by_token


@auth_by_token
def kalenzabot(botCommand:ABotCommand):

    role = get_role(botCommand.channel)
    return execute(botCommand, role)

# de = public access
@auth_by_token
def de(botCommand: ABotCommand):
    return execute(botCommand, BotRole.ALL)


def execute(botCommand, role):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    no_sync_msg = True

    response = botCommand.execute(role)
    logger.info("response:{}".format(response))

    if response.text is not None:
        no_sync_msg = response.send(botCommand.channel)

    if no_sync_msg:
        r = None
    else:
        r = response.text

    return r

