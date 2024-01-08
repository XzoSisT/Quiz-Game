from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class QuizGame(App):
    def build(self):
        self.questions = [
            {"question": "2+2 = ?", "options": ["1", "2", "3", "4"], "answer": "4"},
            {"question": "5+4 = ?", "options": ["9", "3", "7", "4"], "answer": "9"},
            {"question": "2+3 = ?", "options": ["5", "2", "3", "4"], "answer": "5"}
        ]
        self.current_question_index = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.question_label = Label(text="")
        self.option_buttons = [Button(text="", on_press=self.check_answer) for _ in range(4)]

        self.layout.add_widget(self.question_label)
        for button in self.option_buttons:
            self.layout.add_widget(button)

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

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    QuizGame().run()
