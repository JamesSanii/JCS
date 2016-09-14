# Created by: James Sanii
# Created on: September 2016
# Created for: ICS3U
# This program is the Hello, World program, but with 3 buttons

import ui

def hello_world_touch_up_inside_english(sender):
    #print ('Hello, World!')
    view['hello_world_label'].text = ("Hello, World!")

def hello_world_touch_up_inside_french(sender):
    #print ('Bonjour, Monde')
    view['hello_world_label'].text = ("Bonjour, Monde!")
	
def hello_world_touch_up_inside_spanish(sender):
    #print ('Hola Mundo!')
    view['hello_world_label'].text = ("Hola Mundo!")

view = ui.load_view()
view.present('sheet')
