from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
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
            {"question": "Who wrote 'Romeo and Juliet ?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "answer":"William Shakespeare"},
            {"question": "What is the largest mammal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Gorilla"], "answer": "Blue Whale"},
            {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Silver", "Iron"], "answer": "Oxygen"},
            {"question": "In what year did World War II end?", "options": ["1939", "1943", "1945", "1950"], "answer": "1945"},
            {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"},
            {"question": "What is the currency of Japan?", "options": ["Dollar", "Euro", "Yuan", "Yen"], "answer": "Yen"},
            {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7"},
            {"question": "What is the largest ocean?", "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
            {"question": "Who is known as the 'Father of Computer Science'?", "options": ["Alan Turing", "Bill Gates", "Steve Jobs", "Tim Berners-Lee"], "answer": "Alan Turing"},
            {"question": "Which country is known as the 'Land of the Rising Sun'?", "options": ["China", "South Korea", "Japan", "Vietnam"], "answer": "Japan"},
            {"question": "What is the square root of 81?", "options": ["7", "9", "10", "12"], "answer": "9"},
            {"question": "Which gas do plants absorb during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "answer": "Carbon Dioxide"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["J.K. Rowling", "Harper Lee", "George Orwell", "Mark Twain"], "answer": "Harper Lee"},
            {"question": "What is the largest desert in the world?", "options": ["Gobi Desert", "Arabian Desert", "Sahara Desert", "Karakum Desert"], "answer": "Sahara Desert"},
            {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister"], "answer": "Alexander Fleming"},
            {"question": "Which planet is known as the 'Blue Planet'?", "options": ["Earth", "Uranus", "Neptune", "Jupiter"], "answer": "Earth"},
            {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "answer": "Canberra"},
            {"question": "Who painted 'Starry Night'?", "options": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Edvard Munch"], "answer": "Vincent van Gogh"},
            {"question": "What is the speed of light?", "options": ["300,000 km/s", "500,000 km/s", "700,000 km/s", "1,000,000 km/s"], "answer": "300,000 km/s"},
            {"question": "In which year did the Titanic sink?", "options": ["1905", "1912", "1920", "1931"], "answer": "1912"},
            {"question": "Who is the author of '1984'?", "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick"], "answer": "George Orwell"},
            {"question": "What is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "2"},
            {"question": "Who discovered gravity?", "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Johannes Kepler"], "answer": "Isaac Newton"},
            {"question": "What is the capital of Brazil?", "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"], "answer": "Brasília"},
            {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"], "answer": "Alexander Graham Bell"},
            {"question": "What is the largest bird in the world?", "options": ["Eagle", "Ostrich", "Penguin", "Albatross"], "answer": "Ostrich"},
            {"question": "In what year did the Berlin Wall fall?", "options": ["1985", "1989", "1991", "1995"], "answer": "1989"},
            {"question": "Who composed 'Moonlight Sonata'?", "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert"], "answer": "Ludwig van Beethoven"},
            {"question": "What is the boiling point of water in Celsius?", "options": ["0°C", "50°C", "100°C", "150°C"], "answer": "100°C"},
            {"question": "Who was the first woman to win a Nobel Prize?", "options": ["Marie Curie", "Mother Teresa", "Rosalind Franklin", "Dorothy Crowfoot Hodgkin"], "answer": "Marie Curie"},
            {"question": "What is the largest fish in the world?", "options": ["Tuna", "Shark", "Whale Shark", "Salmon"], "answer": "Whale Shark"},
            {"question": "In what year did the Apollo 11 mission land on the moon?", "options": ["1961", "1969", "1975", "1980"], "answer": "1969"},
            {"question": "Who wrote 'The Great Gatsby'?", "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "J.D. Salinger", "John Steinbeck"], "answer": "F. Scott Fitzgerald"},
            {"question": "What is the largest flower in the world?", "options": ["Sunflower", "Rose", "Orchid", "Rafflesia"], "answer": "Rafflesia"},
            {"question": "Who is known as the 'Queen of Pop'?", "options": ["Madonna", "Beyoncé", "Lady Gaga", "Katy Perry"], "answer": "Madonna"},
            {"question": "What is the speed of sound?", "options": ["300 m/s", "500 m/s", "700 m/s", "1,000 m/s"], "answer": "343 m/s"},
            {"question": "Who wrote 'The Catcher in the Rye'?", "options": ["J.D. Salinger", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck"], "answer": "J.D. Salinger"},
            {"question": "What is the capital of South Africa?", "options": ["Cape Town", "Durban", "Johannesburg", "Pretoria"], "answer": "Pretoria"},
            {"question": "Who painted 'The Persistence of Memory'?", "options": ["Salvador Dalí", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], "answer": "Salvador Dalí"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
            {"question": "Who is the author of 'The Lord of the Rings' trilogy?", "options": ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "C.S. Lewis"], "answer": "J.R.R. Tolkien"}
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
        self.question_number_label = Label(text="", color=(0, 0, 0, 1))
        self.layout.add_widget(self.question_number_label)
        self.sound_correct = SoundLoader.load('correct-2-46134.mp3')  
        self.sound_wrong = SoundLoader.load('negative_beeps-6008.mp3')
        self.music = SoundLoader.load('gamemusic-6082.mp3')
        self.music.loop = True
        self.total_questions = len(self.questions)
        self.questions_per_round = 10
        self.questions_in_current_round = []
       
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

        self.start_music()
        self.display_question_set()
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

    def start_music(self):
        if self.music:
            self.music.play()

    def stop_music(self):
        if self.music:
            self.music.stop()
    
    def display_question(self):
        if not self.questions_in_current_round or self.current_question_index >= len(self.questions_in_current_round):
            self.show_popup("Game Over", f"Your final score: {self.score}")
            self.reset_game()
            return

        question_data = self.questions_in_current_round[self.current_question_index]
        self.question_label.text = question_data["question"]
        options = random.sample(question_data["options"], len(question_data["options"]))

        for button, option in zip(self.option_buttons, options):
            button.text = option

        for button in self.option_buttons:
            button.disabled = False

        self.question_number_label.text = f"Question {self.current_question_index + 1}/{len(self.questions_in_current_round)}"


    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = self.questions_in_current_round[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            instance.disabled = True
            self.sound_correct.play()
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.sound_wrong.play()
                self.show_popup("Game Over", f"You're out of attempts! Your final score: {self.score}")
                self.reset_game()
            self.sound_wrong.play()
        
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
        self.stop_music()
        App.get_running_app().stop()

    def dismiss_menu(self):
        self.menu_popup.dismiss()

    def reset_game(self):
        self.current_question_index = 0
        self.score = 0
        self.attempts_left = 5
        self.total_time = 0
        self.display_question_set()
        self.start_music()
        self.display_question_set()

    def display_question_set(self):
        self.questions_in_current_round = random.sample(self.questions, self.questions_per_round)
        self.current_question_index = 0
        self.display_question()
    
    def next_question(self, instance):
        if self.current_question_index < len(self.questions_in_current_round) - 1:
            self.current_question_index += 1
            self.display_question()
            self.question_number_label.text = f"Question {self.current_question_index + 1}/{len(self.questions_in_current_round)}"
        else:
            self.show_popup("Game Over", f"Your final score: {self.score}")
            self.next_button.disabled = True

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