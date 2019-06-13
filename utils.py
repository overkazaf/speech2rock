import os, time

def cmd_say(msg):
	os.system("echo '{}' | say".format(msg))

def count_down_by_seconds(num):
	while num > 0:
		print("还剩{}秒".format(num))
		num=num - 1
		time.sleep(1)
	print('录制结束')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()