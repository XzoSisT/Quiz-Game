from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class QuizGame(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.question_label = Label(text="")

if __name__ == '__main__':
    QuizGame().run()
