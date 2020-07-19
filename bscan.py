import kivy
import subprocess
from kivy.app import App
kivy.require('1.11.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty, ListProperty, StringProperty
import fileinput
import sys
import re
import os, signal

# Setting size to resizable
Config.set('graphics', 'resizable', 1)

## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')


##class Populate:
##    def __init__(self, numb):
##        with open("path/to/the/ini/file", "r") as f:
##            dat = f.readlines()
##            self.numb = dat[5]
##    def myfunc(self):
##        print(self.numb)
##p1 = Populate(numb)
##p1.myfunc()

# Creating a Layout class
class BscanLayout(GridLayout):
##    with open("path/to/the/ini/file", "r") as f:
##        dat = f.readlines()
##        display1 = dat[5]
##        print(display1)        
    # Function called when update is pressed
##    def load(self, display1):
##        with open("path/to/the/ini/file", "r") as f:
##            dat = f.readlines()
##            display1 = dat[5]
##            print(display1)
    def parameters(self, data):

        with open("path/to/the/ini/file", "r") as file:
            #read a list of lines into data
            data = file.readlines()
        data[3] = self.display.text+'\n'
        data[4] = "#Exposure_time_in_microsec\n"
        data[5] = self.display1.text+'\n'
        data[8] = "#Width_upto_1440\n"
        data[9] = self.display2.text+'\n'
        data[10] = "#Height_upto_1080\n"
        data[11] = self.display3.text+'\n'
        data[33] = self.display4.text+'\n'
        data[17] = self.display27.text+'\n'
        data[35] = self.display26.text+'\n'

        with open("path/to/the/ini/file", "w") as file:
            file.writelines( data )

# Creating another class for the advanced settings screen

class AdvSettings(GridLayout):


    def parameters1(self, data):
        with open("path/to/the/ini/file", "r") as file:
            #read a list of lines into data
            data = file.readlines()


        data[7] = self.display6.text+'\n'
        data[13] = self.display7.text+'\n'
        data[15] = self.display8.text+'\n'
        data[19] = self.display9.text+'\n'
        data[21] = self.display10.text+'\n'
        data[25] = self.display11.text+'\n'
        data[27] = self.display11a.text+'\n'
        data[29] = self.display11b.text+'\n'
        data[31] = self.display11c.text+'\n'
        data[23] = self.display12.text+'\n'
        data[37] = self.display13.text+'\n'
        data[39] = self.display14.text+'\n'
        data[41] = self.display15.text+'\n'
        data[43] = self.display16.text+'\n'
        data[45] = self.display17.text+'\n'
        data[47] = self.display18.text+'\n'
        data[49] = self.display19.text+'\n'
        data[51] = self.display20.text+'\n'
        data[53] = self.display21.text+'\n'
        data[55] = self.display22.text+'\n'
        data[57] = self.display23.text+'\n'
        data[59] = self.display24.text+'\n'
        data[61] = self.display25.text+'\n'


        with open("path/to/the/ini/file", "w") as file:
            file.writelines( data )


class BscanLayoutScreen(Screen):
    pass

class AdvSettingsScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


# Creating App class (very important!)
class BscanApp(App):
    with open("path/to/the/ini/file", "r") as f:
        dat = f.readlines()
        disp = dat[3]

        disp1 = dat[5]
        disp2 = dat[9]
        disp3 = dat[11]
        disp4 = dat[33]
        disp6 = dat[7]
        disp7 = dat[13]
        disp8 = dat[15]
        disp9 = dat[19]
        disp10 = dat[21]
        disp11 = dat[25]
        disp11a = dat[27]
        disp11b = dat[29]
        disp11c = dat[31]
        disp12 = dat[23]
        disp13 = dat[37]
        disp14 = dat[39]
        disp15 = dat[41]
        disp16 = dat[43]
        disp17 = dat[45]
        disp18 = dat[47]
        disp19 = dat[49]
        disp20 = dat[51]
        disp21 = dat[53]
        disp22 = dat[55]
        disp23 = dat[57]
        disp24 = dat[59]
        disp25 = dat[61]
        disp26 = dat[35]
        disp27 = dat[17]

    def execute(self):
        s = subprocess.check_call("path/to/the/bin/directory/; ./BscanFFTspinjnt.bin", shell = True)  #runs BscanFFTspinjnt
    def build(self):
        return ScreenManagement()

# Creating object and running it
bscanApp = BscanApp()
bscanApp.run()
