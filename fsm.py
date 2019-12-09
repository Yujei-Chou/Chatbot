from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import AQIParse
from utils import testfcn
import requests
import urllib3

county=[]
sitename=[]
AQI=[]
query_SiteIdx=[]
query_AQI=0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        requests.packages.urllib3.disable_warnings()
        url = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json",verify=False)
        dicts = url.json()

        for data in dicts:
            county.append(data["County"])
            sitename.append(data["SiteName"])
            AQI.append(data["AQI"])

        print("=============test===============")


    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "hi"
            


    def is_going_to_County(self, event):
        text = event.message.text
        
        if "查詢空氣品質" in text:
            print(len(county))
            return True

    def is_going_to_Sitename(self, event):
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
    
    def is_going_to_AQI(self, event):
        text = event.message.text
        try:
            idx = sitename.index(text)
        except ValueError:
            idx = -1
        
        print(idx)
        if idx != -1:
            query_AQI = idx
            return True
        else:
            return False


    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "Hello")
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    
    def on_enter_County(self, event):
        print("I'm entering County")

        reply_token = event.reply_token
        temp = "請輸入想要查詢的縣市"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_County(self, event):
        print("Leaving County")


    def on_enter_Sitename(self, event):
        print("I'm entering Sitename")

        reply_token = event.reply_token
        temp = "請選擇想要查詢的地區:\n"
        
        for j in range(0,len(query_SiteIdx)):
            temp=temp+sitename[query_SiteIdx[j]]+"\n"
        
        send_text_message(reply_token, temp)
        #self.go_back()

    def on_exit_Sitename(self):
        print("Leaving Sitename")

    def on_enter_AQI(self, event):
        print("I'm entering AQI")

        reply_token = event.reply_token
        temp = AQI[query_AQI]
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_AQI(self):
        print("Leaving AQI")

