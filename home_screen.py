screen_home = """
Screen:
    MDBottomNavigation:
        # This is a fancy Manager
        MDBottomNavigationItem:
            # This is a home screen
            text: "Home"
            name: "home"
            icon: "home"
            MDNavigationLayout:
                ScreenManager:
                    Screen:
                        MDBoxLayout:
                            orientation: 'vertical'
                            MDTopAppBar: 
                                title: 'Home'
                                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                                elevation: 8
                            Widget:
#                    MDBottomAppBar:
#                        MDTopAppBar: 
#                            title: 'Help'
#                            left_action_items: [["menu", lambda x: app.navigation_draw()]]
#                            mode: 'end'
#                            icon: 'plus'
#                            type: 'bottom'
#                            on_action_button: app.navigation_draw()
                MDNavigationDrawer:
                    id: nav_drawer

                    ContentNavigationDrawer:
                        orientation: 'vertical'
                        
                        ScrollView:
                            DrawerList:
                                id: md_list
                                
                                MDList:
                                    OneLineIconListItem:
                                        text: 'Connections' 
                                        
                                        IconLeftWidget:
                                            icon: 'lan-connect'
                                    
                                    OneLineIconListItem:
                                        text: 'Units'
                                    
                                        IconLeftWidget:
                                            icon: 'folder'



        MDBottomNavigationItem:
            # This is a new screen
            text: "New"
            name: "new"
            icon: "plus"

#        MDLabel:
#            text: 'Hello World'
#            halign: 'center'
#            theme_text_color: 'Custom'
#            text_color: 255/255.0, 84/255.0, 0, 1
#        
#        MDBottomAppBar:
#            MDTopAppBar: 
#                title: 'Help'
#                left_action_items: [["menu", lambda x: app.navigation_draw()]]
#                mode: 'end'
#                icon: 'plus'
#                type: 'bottom'
#                on_action_button: app.navigation_draw()
"""
