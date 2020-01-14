#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telegram_button
import os
import sys

def test():
	# telegram_button.gen(news_source='bbc')
	pdf_name = telegram_button.gen(news_source='bbc英文')
	os.system('open %s -g' % pdf_name)
	
test()