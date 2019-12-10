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
query_AQIidx=0
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
            return False

    def is_going_to_result(self, event):
        text = event.message.text
        try:
            idx = sitename.index(text)
        except ValueError:
            idx = -1

        print(idx)
        if idx != -1:
            global query_AQIidx
            query_AQIidx = idx
            print("query_AQIidx:"+str(query_AQIidx))
            return True
        else:
            return False

    def is_going_to_health(self, event):
        text = event.message.text
        if "aqi:" and "對健康影響" in text.lower():
            global query_AQI
            query_AQI = int(text.split(":")[1].split(" ")[0])
            print("query_AQI:"+ str(query_AQI))
            return True
        else:
            return False

    def is_going_to_activity(self, event):
        text = event.message.text
        if "aqi:" and "活動建議" in text.lower():
            global query_AQI
            query_AQI = int(text.split(":")[1].split(" ")[0])
            print("query_AQI:"+ str(query_AQI))
            return True
        else:
            return False


    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        temp="1.輸入 查詢空氣品質 ,可查各地區的AQI值\n" + "2.輸入 AQI:(你要查詢的值) 對健康影響\n" + "3.輸入AQI:(你要查詢的值) 活動建議" 
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    def on_enter_health(self, event):
        print("I'm entering health")
        
        reply_token = event.reply_token
        if query_AQI > 0 and query_AQI < 51:
            send_img_message(reply_token, "https://i.imgur.com/MYOHzSm.png","https://i.imgur.com/MYOHzSm.png")
        elif query_AQI > 50 and query_AQI < 101:
            send_img_message(reply_token, "https://i.imgur.com/iGusRai.png","https://i.imgur.com/iGusRai.png")
        elif query_AQI > 100 and query_AQI < 151:
            send_img_message(reply_token, "https://i.imgur.com/SIGvkCI.png","https://i.imgur.com/SIGvkCI.png")
        elif query_AQI > 150 and query_AQI < 201:
            send_img_message(reply_token, "https://i.imgur.com/Z7mIFcf.png","https://i.imgur.com/Z7mIFcf.png")
        elif query_AQI > 200 and query_AQI < 301:
            send_img_message(reply_token, "https://i.imgur.com/Wsq0301.png","https://i.imgur.com/Wsq0301.png")
        elif query_AQI > 300 and query_AQI < 501:
            send_img_message(reply_token, "https://i.imgur.com/CppbGvu.png","https://i.imgur.com/CppbGvu.png")
        self.go_back()

    def on_exit_health(self):
        print("Leaving health")

    def on_enter_activity(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        if query_AQI > 0 and query_AQI < 51:
            send_img_message(reply_token, "https://i.imgur.com/ElmmU7K.png","https://i.imgur.com/ElmmU7K.png")
        elif query_AQI > 50 and query_AQI < 101:
            send_img_message(reply_token, "https://i.imgur.com/TPKRAvH.png","https://i.imgur.com/TPKRAvH.png")
        elif query_AQI > 100 and query_AQI < 151:
            send_img_message(reply_token, "https://i.imgur.com/l9XaGMb.png","https://i.imgur.com/l9XaGMb.png")
        elif query_AQI > 150 and query_AQI < 201:
            send_img_message(reply_token, "https://i.imgur.com/bCW1uyB.png","https://i.imgur.com/bCW1uyB.png")
        elif query_AQI > 200 and query_AQI < 301:
            send_img_message(reply_token, "https://i.imgur.com/id9r6a7.png","https://i.imgur.com/id9r6a7.png")
        elif query_AQI > 300 and query_AQI < 501:
            send_img_message(reply_token, "https://i.imgur.com/kaznQOc.png","https://i.imgur.com/kaznQOc.png")
        self.go_back()

    def on_exit_activity(self):
        print("Leaving activity")

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
        temp = "AQI值:" + AQI[query_AQIidx]

        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_result(self):
        print("Leaving result")

    


