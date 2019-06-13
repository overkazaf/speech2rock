#!/bin/python
# -*- coding: utf-8 -*-

import sys, os
from aip import AipSpeech
from wav2pcm import wav_to_pcm
import keyboard, time
from baidu_client import get_client
from utils import get_file_content, cmd_say

client = get_client()
def parse_voice_file(filename):
	cmd_say('开始解析语音文件')
	
	newFilePath = wav_to_pcm(filename)
	
	print("Handling file ", filename)
	
	# 通过百度语音识别API识别本地录制并已转化的语音文件
	resp = client.asr(get_file_content(newFilePath), 'pcm', 16000, {
	    'dev_pid': 1536,
	})

	print("AI response:", resp)
	print("")

	result = resp['result']

	cmd_texts = []
	for r in result:
		print(r)
		cmd_texts.append(r)
		cmd_say(u"文件解析的结果是 {}".format(r))

	for text in cmd_texts:
		# We can implement some strategies here
		if '音乐' in text:
			cmd_say("检测到有'音乐'这个关键字，正在打开音乐...")
			os.system("open -a NeteaseMusic")
			time.sleep(2)
			# 播放，需要设置全局快捷键
			keyboard.press_and_release('ctrl+v')
		else:
			if '浏览器' in text:
				cmd_say("检测到有'浏览器'这个关键字，正在打开Chrome...")
				os.system("open -a Google\ Chrome")
				time.sleep(2)



