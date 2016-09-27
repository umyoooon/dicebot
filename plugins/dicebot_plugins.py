# -*- coding: utf-8 -*-

import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('dice')
@listen_to('dice')
def dice(message):
    random.seed()
    message.reply(str(random.randint(1,99)))
