from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

from home_screen import screen_home

Window.size = (300, 500)


class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
#        self.theme_cls.primary_palette = 'Pink'
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_home)
        return screen
    
    def navigation_draw(self):
        print("Navigation")

DemoApp().run()
