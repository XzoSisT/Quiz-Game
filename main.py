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
            {"question": "Can dragonfly fly ?", "options": ["yes, it can fly", "no, it can't", "unsure", "don't know"], "answer": "yes, it can fly"},
            {"question": "What region is Yala in ?", "options": ["North", "Mid", "South", "Northeastern"], "answer": "South"},
            {"question": "18*99 = ?", "options": ["78", "996", "1789", "1782"], "answer":"1782"},
            {"question": "What is the capital city of France ?", "options": ["Berlin", "London", "Paris", "Madrid"], "answer":"Paris"},
            {"question": "Which planet is known as the Red Planet ?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer":"Mars"},
            {"question": "Who wrote 'Romeo and Juliet ?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "answer":"William Shakespeare"}
        ]
        self.current_question_index = 0
        self.score = 0

        self.menu_button = Button(text="Menu", on_press=self.show_menu, background_color=(0.7, 0.7, 0.7, 1))
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.layout.bind(size=self._update_background)
        self.question_label = Label(text="", color=(0, 0, 0, 1))
        self.option_buttons = [Button(text="", on_press=self.check_answer, background_color=(0.6, 0.6, 0.9, 1)) for _ in range(4)]
        self.next_button = Button(text="Next Question", on_press=self.next_question, background_color=(0.5, 0.8, 0.5, 1))
        self.back_button = Button(text="Previous Question", on_press=self.previous_question, background_color=(0.9, 0.6, 0.6, 1))
        self.total_time = 0
        self.menu_button = Button(text="Menu", on_press=self.show_menu, background_color=(0.7, 0.7, 0.7, 1))
        self.menu_popup = None
        self.attempts_left = 5
       
        self.button_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.button_layout.add_widget(self.menu_button)
        self.button_layout.add_widget(self.back_button)
        self.button_layout.add_widget(self.next_button)

        with self.layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.bg_rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.add_widget(self.question_label)
        for button in self.option_buttons:
            self.layout.add_widget(button)
        self.layout.add_widget(self.button_layout)

        self.display_question()

        self.layout.background_color = (0.9, 0.9, 0.9, 1)
        self.question_label.font_size = '24sp'
        for button in self.option_buttons:
            button.font_size = '20sp'
            button.background_normal = 'button_normal.png'
            button.background_down = 'button_down.png'

        self.layout.padding = [20, 50]
        self.button_layout.size_hint_y = None
        self.button_layout.height = '44dp'

        return self.layout

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.text = question_data["question"]
        options = random.sample(question_data["options"], len(question_data["options"]))

        for button, option in zip(self.option_buttons, options):
            button.text = option

        for button in self.option_buttons:
            button.disabled = False

    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            instance.disabled = True
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.show_popup("Game Over", f"You're out of attempts! Your final score: {self.score}")
                self.reset_game()
        
        self.show_popup("Result", f"Your current score: {self.score}")

    def show_menu(self, instance):
        self.menu_popup = Popup(title="Game Menu", size_hint=(None, None), size=(300, 200))
    
        menu_layout = BoxLayout(orientation='vertical', spacing=10)
    
        resume_button = Button(text="Resume", on_press=self.resume_game)
        restart_button = Button(text="Restart", on_press=self.restart_game)
        exit_button = Button(text="Exit", on_press=self.exit_game)
    
        menu_layout.add_widget(resume_button)
        menu_layout.add_widget(restart_button)
        menu_layout.add_widget(exit_button)
    
        self.menu_popup.content = menu_layout
        self.menu_popup.open()

    def resume_game(self, instance):
        self.dismiss_menu()

    def restart_game(self, instance):
        self.dismiss_menu()
        self.reset_game()

    def exit_game(self, instance):
        App.get_running_app().stop()

    def dismiss_menu(self):
        self.menu_popup.dismiss()

    def reset_game(self):
        self.current_question_index = 0
        self.score = 0
        self.attempts_left = 5
        self.total_time = 0
        self.display_question()
    
    def next_question(self, instance):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question()
        else:
            self.show_popup("Game Over", f"Your final score: {self.score}")

    def previous_question(self, instance):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.display_question()

    def _update_background(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    QuizGame().run()