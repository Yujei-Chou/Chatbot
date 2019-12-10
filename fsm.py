from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_img_message
import requests
import urllib3
import datetime

county=[]
sitename=[]
AQI=[]
query_SiteIdx=[]
query_AQI=0
hour="-1"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"


    def is_going_to_county(self, event):
        global hour
        if hour != datetime.datetime.now().strftime("%H"):
            hour = datetime.datetime.now().strftime("%H")
            county.clear()
            sitename.clear()
            AQI.clear()
            requests.packages.urllib3.disable_warnings()
            url = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json",verify=False)
            dicts = url.json()

            for data in dicts:
                county.append(data["County"])
                sitename.append(data["SiteName"])
                AQI.append(data["AQI"])

        text = event.message.text
        if "查詢空氣品質" in text.lower():
            return True

    def is_going_to_sitename(self, event):
        text = event.message.text
        try:
            idx = county.index(text)
        except ValueError:
            idx = -1

        if idx != -1:
            SitenameIdx=[i for i in range(len(county)) if county[i] == text]    
            for j in range(0,len(SitenameIdx)):
                query_SiteIdx.append(SitenameIdx[j])

            return True
        else:
            # send_text_message(reply_token, "輸入錯誤")
            return False

    def is_going_to_result(self, event):
        text = event.message.text
        try:
            idx = sitename.index(text)
        except ValueError:
            idx = -1

        print(idx)
        if idx != -1:
            global query_AQI
            query_AQI = idx
            print("query_AQI:"+str(query_AQI))
            return True
        else:
            return False

 



    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        temp="輸入查詢空氣品質,可查詢目前各地區的AQI值"
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    
    def on_enter_county(self, event):
        print("I'm entering county")

        reply_token = event.reply_token
        temp = "請輸入想要查詢的縣市"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_county(self, event):
        print("Leaving county")
    
    def on_enter_sitename(self, event):
        print("I'm entering sitename")

        reply_token = event.reply_token
        temp = "請選擇想要查詢的地區:\n"
 
        for j in range(0,len(query_SiteIdx)):
            temp=temp+sitename[query_SiteIdx[j]]+"\n"
        query_SiteIdx.clear()
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_sitename(self, event):
        print("Leaving sitename")

    def on_enter_result(self, event):
        print("I'm entering result")
        reply_token = event.reply_token
        temp = "AQI值:" + AQI[query_AQI]

        send_text_message(reply_token, temp)
        #send_img_message(reply_token, "https://i.imgur.com/iGusRai.png","https://i.imgur.com/iGusRai.png")
        self.go_back()

    def on_exit_result(self):
        print("Leaving result")

    


