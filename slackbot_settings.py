# -*- coding: utf-8 -*-
API_TOKEN = "xoxb-84103026966-xEZsS02k5bpr0GG0RhogJZfs"
DEFAULT_REPLY = "テストだよ"
ERRORS_TO = "hajime"
PLUGINS = [
    'slackbot.plugins',
    'dicebot.plugins',
]


@respond_to('dice')
def dice(message):
    random.seed()
    message.reply(random.randint(1,99))
