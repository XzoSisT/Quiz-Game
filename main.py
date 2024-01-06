from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class QuizGame(App):
    def build(self):
        self.questions = [
            {"question": "2+2 = ?", "options": ["1", "2", "3", "4"], "answer": "4"}
        ]
        self.current_question_index = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.question_label = Label(text="")

if __name__ == '__main__':
    QuizGame().run()
