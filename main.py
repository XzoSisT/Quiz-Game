from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
import random

class QuizGame(App):
    def build(self):
        self.questions = [
            {"question": "2+2 = ?", "options": ["1", "2", "3", "4"], "answer": "4"},
            {"question": "5+4 = ?", "options": ["9", "3", "7", "4"], "answer": "9"},
            {"question": "2+3 = ?", "options": ["5", "2", "3", "4"], "answer": "5"},
            {"question": "It can fly,It like blood and It born in water. What is it ?", "options": ["mosqitoe", "frog" , "ant" , "cat"], "answer": "mosqitoe"},
            {"question": "Can dragonfly fly ?", "options": ["yes,it can fly", "no, it can't", "unsure", "don't know"], "answer": "yes, it can fly"},
            {"question": "What region is Yala in ?", "options": ["North", "Mid", "South", "Northeastern"], "answer": "South"},
            {"question": "18*99 = ?", "options": ["78", "996", "1789", "1782"], "answer":"1782"}
        ]
        self.current_question_index = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.layout.bind(size=self._update_background)
        self.question_label = Label(text="")
        self.option_buttons = [Button(text="", on_press=self.check_answer) for _ in range(4)]
        self.next_button = Button(text="Next Question", on_press=self.next_question)

        with self.layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.bg_rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.add_widget(self.question_label)
        for button in self.option_buttons:
            self.layout.add_widget(button)
        self.layout.add_widget(self.next_button)

        self.display_question()

        return self.layout

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.text = question_data["question"]
        options = random.sample(question_data["options"], len(question_data["options"]))

        for button, option in zip(self.option_buttons, options):
            button.text = option

    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
        
        self.show_popup("Result", f"Your current score: {self.score}")

    def next_question(self, instance):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question()
        else:
            self.show_popup("Game Over", f"Your final score: {self.score}")

    def _update_background(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    QuizGame().run()
