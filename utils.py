import os
import requests
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def AQIParse():
    url = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json",verify=False)
    dicts = url.json()
    matrix=[]
    i=0
    for data in dicts:
        matrix.append([])
        matrix[i].append(data["County"])
        matrix[i].append(data["SiteName"])
        matrix[i].append(data["AQI"])
        i+=1
       
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
