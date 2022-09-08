from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior

Window.size = (300, 500)

host_field = """
MDTextField:
    hint_text: "Host"
    icon_right: "antenna"
    pos_hint: {'center_x':.5, 'center_y':.7}
    size_hint_x: None
    width: 250


"""

port_field = """
MDTextField:
    hint_text: "Port"
    icon_right: "hdmi-port"
    pos_hint: {'center_x':.5, 'center_y':.6}
    size_hint_x: None
    width: 250

"""
webport_field = """
MDTextField:
    hint_text: "Webport"
    icon_right: "webhook"
    pos_hint: {'center_x':.5, 'center_y':.5}
    size_hint_x: None
    width: 250

"""

class DemoApp(MDApp):
    def login_button(self):
        button = MDRectangleFlatButton(text='Log-in', pos_hint={'center_x': .5, 'center_y': .4}, on_release=self.show_warning)
        return button

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.host = Builder.load_string(host_field)
        self.port = Builder.load_string(port_field)
        self.web_port = Builder.load_string(webport_field)
        button_login = self.login_button()
        screen.add_widget(self.host)
        screen.add_widget(self.port)
        screen.add_widget(self.web_port)
        screen.add_widget(button_login)
        return screen

    def show_warning(self, obj):
        if self.host.text is "":
            check_string = 'Please enter a host'
        elif self.port.text is "": 
            check_string = 'Please enter a port'
        elif self.web_port.text is "":
            check_string = 'Please enter a Webport'
        close_button = MDFlatButton(text='close', theme_text_color='Custom', text_color=self.theme_cls.primary_color, on_release=self.close_dialog)
        self.dialog = MDDialog(title='WARNING', text=check_string, size_hint=(0.7, 1), buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
