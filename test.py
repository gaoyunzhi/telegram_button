#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telegram_button
import os
import sys
import yaml
from telegram.ext import Updater
import traceback as tb

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)

tele = Updater(CREDENTIALS['bot_token'], use_context=True)
debug_group = tele.bot.get_chat(-1001198682178)

@log_on_fail(debug_group)
def like(update, context):
	try:
		key = '%d/%d' % (update.message.chat.id, update.message.id)
		user = update.from_user.id
	except Exception as e:
		tb.print_exc()
		print(e)

tele.dispatcher.add_handler(CallbackQueryHandler(like, pattern="like"))

test_group = tele.bot.get_chat(-369602734)

reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('👍', callback_data='like')]])
test_group.send_message(text='test message',reply_markup=reply_markup)

tele.start_polling()
