from aip import AipSpeech
from baidu_config import get_config

def get_client():
	[APP_ID, API_KEY, SECRET_KEY] = get_config()
	return AipSpeech(APP_ID, API_KEY, SECRET_KEY)
