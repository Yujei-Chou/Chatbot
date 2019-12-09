from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import AQIParse



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "hi"
            


    def is_going_to_County(self, event):
        text = event.message.text
        if text.lower() == "start":
            return True

    def is_going_to_result(self, event):
        text = event.message.text
        if "yes" in text.lower():
            # 爬蟲
            return True
        else:
            send_text_message(reply_token, "哈哈哈")
            # 爬蟲
            return True

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"



    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "Hello")
        self.go_back()

    def on_exit_menu(self):
        print("Leaving state1")

    
    def on_enter_County(self, event):
        print("I'm entering end")

        reply_token = event.reply_token
        temp = "Do you want to see movie?"
        send_text_message(reply_token, temp)
        # self.go_back()

    def on_exit_County(self, event):
        print("Leaving end")


    def on_enter_result(self, event):
        print("I'm entering result")

        reply_token = event.reply_token
        temp = "which movie?"
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_result(self):
        print("Leaving result")

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()
