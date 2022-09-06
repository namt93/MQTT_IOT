from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar: 
            title: 'Demo Application'
        MDLabel:
            text: 'Hello World'
            halign: 'center'

"""

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
