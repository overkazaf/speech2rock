#!/bin/python
# -*- coding: utf-8 -*-

import os, sys
from baidu_client import get_client

# 通过百度API进行文字的语音合成
def compose_voice_file_and_play(text):
	result  = get_client().synthesis(text, 'zh', 1, {
	    'vol': 5,
	})

	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
	    with open('audio.mp3', 'wb') as f:
	        f.write(result)
	        os.system('afplay audio.mp3')