import os
import logging
from BotCommands.BotResponse import BotResponse



class BotRole:
    NONE="NONE",
    DE="DE",
    MANAGERS="MANAGERS",
    ALL="ALL"

class ABotCommand:

    def __init__(self, text=None):
        self.text = text
        self.token = None
        self.channel = None

    def execute(self, role:BotRole) -> BotResponse:
        br = BotResponse('', '', self.text)
        return br


