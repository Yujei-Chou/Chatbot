from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import THSRparse

theDay=''
startStation=''
endStation=''
timeSelect=''
payload = {
    'startStation':startStation,
    'endStation':endStation,
    'theDay':theDay,
    'timeSelect':timeSelect,
    'waySelect':'DepartureInMandarin'
}
station = {
    'start':'',
    'sen':''
}


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "嗨"



    def is_going_to_timetable(self, event):
        text = event.message.text
        if "查詢" in text.lower():
            return True
        else:
            return false

        # return text.lower() == "查詢高鐵時刻表"

    def is_going_to_date(self, event):
        text = event.message.text
        if "/" in text.lower():
            theDay = text.lower()
            payload['theDay']=theDay
            return True
        else:
            return false

    def is_going_to_time(self, event):
        text = event.message.text
        if ":" in text.lower():
            timeSelect = text.lower()
            payload['timeSelect']=timeSelect
            return True
        else:
            return false

    def is_going_to_start(self, event):
        text = event.message.text
        if "南港" in text.lower() or "台北" in text.lower() or "板橋" in text.lower() or "桃園" in text.lower() or "新竹" in text.lower() or "苗栗" in text.lower() or "台中" in text.lower() or "彰化" in text.lower() or "雲林" in text.lower() or "嘉義" in text.lower() or "台南" in text.lower() or "左營" in text.lower():
            start = text.lower()
            station['start'] = start
            if start=='南港':
                startStation='2f940836-cedc-41ef-8e28-c2336ac8fe68'
            elif start=='台北':
                startStation='977abb69-413a-4ccf-a109-0272c24fd490'
            elif start=='板橋':
                startStation='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
            elif start=='桃園':
                startStation='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
            elif start=='新竹':
                startStation='a7a04c89-900b-4798-95a3-c01c455622f4'
            elif start=='苗栗':
                startStation='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
            elif start=='台中':
                startStation='3301e395-46b8-47aa-aa37-139e15708779'
            elif start=='彰化':
                startStation='38b8c40b-aef0-4d66-b257-da96ec51620e'
            elif start=='雲林':
                startStation='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
            elif start=='嘉義':
                startStation='60831846-f0e4-47f6-9b5b-46323ebdcef7'
            elif start=='台南':
                startStation='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
            elif start=='左營':
                startStation='f2519629-5973-4d08-913b-479cce78a356'
            payload['startStation']=startStation
            return True
        else:
            return false

    def is_going_to_end(self, event):
        text = event.message.text
        if "南港" in text.lower() or "台北" in text.lower() or "板橋" in text.lower() or "桃園" in text.lower() or "新竹" in text.lower() or "苗栗" in text.lower() or "台中" in text.lower() or "彰化" in text.lower() or "雲林" in text.lower() or "嘉義" in text.lower() or "台南" in text.lower() or "左營" in text.lower():
            end = text.lower()
            station['end'] = end
            if end=='南港':
                endStation='2f940836-cedc-41ef-8e28-c2336ac8fe68'
            elif end=='台北':
                endStation='977abb69-413a-4ccf-a109-0272c24fd490'
            elif end=='板橋':
                endStation='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
            elif end=='桃園':
                endStation='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
            elif end=='新竹':
                endStation='a7a04c89-900b-4798-95a3-c01c455622f4'
            elif end=='苗栗':
                endStation='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
            elif end=='台中':
                endStation='3301e395-46b8-47aa-aa37-139e15708779'
            elif end=='彰化':
                endStation='38b8c40b-aef0-4d66-b257-da96ec51620e'
            elif end=='雲林':
                endStation='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
            elif end=='嘉義':
                endStation='60831846-f0e4-47f6-9b5b-46323ebdcef7'
            elif end=='台南':
                endStation='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
            elif end=='左營':
                endStation='f2519629-5973-4d08-913b-479cce78a356'
            payload['endStation']=endStation
            return True
        else:
            return false

    def is_going_to_result(self, event):
        text = event.message.text
        if "是" in text.lower() or "沒錯" in text.lower() or "對" in text.lower():
            # 爬蟲
            return True
        else:
            send_text_message(reply_token, "哈哈哈")
            # 爬蟲
            return True

 



    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        temp="我是高鐵服務機器人！\n"+"我可以查詢高鐵時刻表~\n"+"請輸入 : 查詢"
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving state1")


    def on_enter_timetable(self, event):
        print("I'm entering timetable")

        reply_token = event.reply_token
        temp="請問你要幾號搭車呢？\n"+"輸入格式為 : YYYY/MM/DD"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_timetable(self, event):
        print("Leaving timetable")


    def on_enter_date(self, event):
        print("I'm entering date")

        reply_token = event.reply_token
        temp = "好的，搭車日期為: " + payload['theDay'] +"\n那你要幾點出發呢？"+"輸入格式為\nhh:mm"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_date(self, event):
        print("Leaving date")


    def on_enter_time(self, event):
        print("I'm entering time")

        reply_token = event.reply_token
        temp = "好的，搭車時間為: " + payload['timeSelect'] +"\n那你要從哪一站出發呢？"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_time(self, event):
        print("Leaving time")
    
    def on_enter_start(self, event):
        print("I'm entering start")

        reply_token = event.reply_token
        temp = "好的，出發車站為: " + station['start'] +"\n那你要搭到哪一站呢？"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_start(self, event):
        print("Leaving start")
    
    def on_enter_end(self, event):
        print("I'm entering end")

        reply_token = event.reply_token
        temp = "好的，抵達車站為: " + station['end'] +"\n以上搭車資訊是否正確?"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_end(self, event):
        print("Leaving end")


    def on_enter_result(self, event):
        print("I'm entering result")

        reply_token = event.reply_token
        result = THSRparse(payload)
        temp = ""
        for i in result:
            temp += i
            temp += "\n"
       
        temp += "\n繼續查詢，請輸入: 查詢"
        temp +="\n\n官網:http://www.thsrc.com.tw/index.html"
        
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_result(self):
        print("Leaving result")

    


