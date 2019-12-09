import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import requests
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def THSRparse(payload):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResult",data=payload,headers=headers)
    soup=BeautifulSoup(res.text,features="html.parser")
    
    trainData=[]
    flag=0

    flag=0
    divs = soup.find_all('div', class_='ui-block-b')
    for d in divs:
    #     print(d)
    #     print(d.string.strip())
        trainData.append(d.string.strip())
        flag+=1
        if flag>10:
            break


    # for i in trainData:
    #     print(i)
    return trainData


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
