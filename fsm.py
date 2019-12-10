from transitions.extensions import GraphMachine

from utils import send_text_message
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


    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "hi"


    def is_going_to_county(self, event):
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
        if "大園" in text.lower():
            # 爬蟲
            return True
        else:
            send_text_message(reply_token, "哈哈哈")
            # 爬蟲
            return True

 



    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        temp="Hello"
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    
    def on_enter_county(self, event):
        print("I'm entering county")

        reply_token = event.reply_token
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
        temp = "wait for second"
 
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_result(self):
        print("Leaving result")

    


