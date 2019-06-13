#!/bin/python
# -*- coding: utf-8 -*-
import sys, os
import sounddevice as sd
from scipy.io.wavfile import write
from translate_voice import parse_voice_file
import threading
import time
from compose import compose_voice_file_and_play
from utils import cmd_say, count_down_by_seconds

fs = 44100  # 采样率
seconds = 3  # 录制时间
if len(sys.argv) == 2:
	seconds = int(sys.argv[1])

compose_voice_file_and_play('请在听到三声滴后开始录制，录制时间一共{}秒，滴滴滴'.format(str(seconds)))

rec_contents = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
 
count_down_by_seconds(seconds)

sd.wait()  # Wait until recording is finished

target_wav_file = 'output/test.wav'
write(target_wav_file, fs, rec_contents)  # Save as WAV file

cmd_say('录制结束')

parse_voice_file(target_wav_file)
