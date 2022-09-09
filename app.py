from kivymd.app import MDApp, App
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDFloatingActionButton
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList


Window.size = (300, 500)


class LoginScreen(Screen, MDApp):
    check_string = ""
    def login_button_click(self):
        if self.ids.host_input.text is "":
            self.check_string = 'Please enter a host'
        elif self.ids.port_input.text is "": 
            self.check_string = 'Please enter a port'
        elif self.ids.webport_input.text is "":
            self.check_string = 'Please enter a Webport'
        if self.check_string is "":
            self.manager.current = 'home'
        else:
            close_button = MDFlatButton(text='close', theme_text_color='Custom', text_color=self.theme_cls.primary_color, on_release=self.close_dialog)
            self.dialog = MDDialog(title='WARNING', text=self.check_string, size_hint=(0.7, 1), buttons=[close_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.check_string = ""
        self.dialog.dismiss()


class HomeScreen(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass



class MQTTScreenManager(ScreenManager):
    pass

class DemoApp(MDApp):
    def build(self):
        kv_file=Builder.load_file('Screen_manager.kv')
        return kv_file
DemoApp().run()
