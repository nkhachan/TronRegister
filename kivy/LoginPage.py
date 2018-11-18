from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from Login import *

Builder.load_file('kv_files/login.kv')


class LoginPage(BoxLayout):
    def __init__(self):
        self.lbl = Label(text="You failed, try again")
        self.registerPageButton = Button(text="Register", on_release=self.registerPage)


    def verify_credentials(self):

        if login(self.ids["username"].text, self.ids["passwd"].text):
            print("Success")
            self.remove_widget(self.lbl)
            self.remove_widget(self.registerPageButton)
            
        elif self.lbl not in self.children:
                self.add_widget(self.lbl)
                self.add_widget()

    def registerPage(self, instance):
        getAddress = TextInput(text="Address")
        if (len(self.children)):
            pass
        self.add_widget(getAddress)
