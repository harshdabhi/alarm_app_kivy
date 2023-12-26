# main.py
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.core.window import Window
from datetime import datetime
import firebase_admin
from firebase_admin import credentials,db,storage
from kivy.clock import Clock
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader


style="""

ScreenManager:
    MainMenu:
    LoginPage:
    PasswordResetDialog:
    ChatScreen:
    AlarmScreen:

    
<MainMenu>:
    name: "main"


    MDLabel:
        text: "ALARM"
        font_size: "30sp"
        pos_hint: {"center_x": .5, "center_y": .935}
        halign: "center"
        bold: True

    MDIconButton:
        icon: "plus"
        pos_hint: {"center_x": .87, "center_y": .94}
        md_bg_color: 0, 0, 0, 1
        theme_text_color: "Custom" 
        text_color: 1, 1, 1, 1
        on_release: app.time_picker()

    MDLabel:
        id:alarm
        text: ""
        pos_hint: {"center_x": .5}
        halign: "center"
        font_size: "30sp"
        bold: True

    MDRaisedButton:
        text: "STOP"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: app.stop()

    

    
    

"""
# Window.size = (350, 600)
class LoginPage(Screen):
    pass

class MainMenu(Screen):
    pass

class ChatScreen(Screen):
    pass

class PasswordResetDialog(Screen):
    pass

class AlarmScreen(Screen):
    pass


class SmartFarm(MDApp):

    sound=SoundLoader.load("alarm.wav")
    volume=0

    def build(self):
            self.theme_cls.theme_style = "Dark"
            if platform == "android":
                self.start_service()
            return Builder.load_string(style)
    

    def time_picker(self):
        # if platform == "android":
            time_dialog = MDTimePicker()
            time_dialog.bind(time=self.get_time,on_save=self.schedule)
            time_dialog.open()
        # else:
        #     pass

    def date_picker(self):
        # if platform == "android":
            date_dialog = MDDatePicker()
            date_dialog.bind(date=self.get_date,on_save=self.schedule)
            date_dialog.open()
       

    def get_time(self, instance, time):
        self.root.get_screen("main").ids.alarm.text = str(time)
        print(time)


    def schedule(self, *args):
        Clock.schedule_once(self.set_alarm, 1)
        Clock

    def set_alarm(self,*args):
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if self.root.get_screen("main").ids.alarm.text == str(current_time):
                self.start()
                break

    def start(self, *args):
        self.sound.play()
        # self.set_volume()

    # def set_volume(self, *args):
    #     self.volume +=0.05
    #     if self.volume < 1:
    #         Clock.schedule_interval(self.set_volume, 10)
    #         self.sound.set_volume(self.volume)
    #         print(self.volume)

    #     else:
    #         self.sound.set_volume(1)
    #         print("max volume")
        

    def stop(self, *args):
        self.sound.stop()
        # Clock.unschedule(self.set_volume)
        Clock.unschedule()

        self.volume = 0

   


SmartFarm().run()