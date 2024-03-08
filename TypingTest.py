import datetime
import random
from tkinter import *


class TypingTest:
    def __init__(self, num, font, color):
        self.phrase = []  # store the randomly selected words here
        self.phrase_labels = []  # store tkinter labels for each word here
        self.window = Tk()
        self.text_box = None
        self.start_time = None
        self.end_time = None
        self.number_of_words = num
        self.font = font
        self.color = color


    def get_phrase(self):
        # Read the words to type from a list of common English words
        with open('words_en.txt') as file:
            words = file.read().split()

        # build a random phrase from the imported word list
        while len(self.phrase) < 20:
            self.phrase.append(random.choice(words))

    def open_window(self, app_name):
        # open tkinter window
        self.window.title(app_name)
        self.window.minsize(width=1000, height=600)
        self.window.config(padx=20, pady=20, bg=self.color)

    def build_phrase_labels(self):
        # iterate through all words
        for i, word in enumerate(self.phrase):
            if i % 5 == 0:  # every fifth word starting at 0, create a frame
                if i > 0:  # close the previous frame before opening a new one
                    phrase_frame.pack()
                phrase_frame = Frame(self.window, pady=5, bg=self.color)

            # build the labels for tkinter. store them in a list to reference later
            self.phrase_labels.append(Label(phrase_frame, text=word, font=self.font, bg=self.color, fg="black"))
            self.phrase_labels[i].pack(side="left")

            if i == self.number_of_words - 1:  # close the last frame
                phrase_frame.pack()

    def create_text_box(self):
        # UI setup input box for text input
        self.text_box = Text(height=5, width=50, font=self.font, wrap=WORD)
        self.text_box.focus()
        self.text_box.config(pady=20, padx=20)
        self.text_box.pack(pady=30)

    def check_user_input(self, char):
        user_input = self.text_box.get("1.0", "end-1c")
        # split user input into a list
        user_words = user_input.split()

        # record start time if not set
        if not self.start_time:
            self.start_time = datetime.datetime.now()

        # iterate through the user input words, comparing against the word list.
        i = 0
        for i, word in enumerate(user_words):
            if i >= self.number_of_words:
                break
            if word == self.phrase[i]:
                self.phrase_labels[i].config(bg="#ccff00")  # word matches: highlight green
            elif i == len(user_words) - 1:
                self.phrase_labels[i].config(bg="#ffdca2")  # current word: highlight yellow
            else:
                self.phrase_labels[i].config(bg="red")  # word doesn't match: highlight red

        # on correction, change highlight back to grey

        for x in range(i + 1, len(self.phrase)):
            self.phrase_labels[x].config(bg=self.color)  # change back to grey

        # end when the last word typed matches the length of the last word expected.
        if (len(user_words) == self.number_of_words and len(user_words[-1]) == len(self.phrase[-1])) or len(
                user_words) > self.number_of_words:
            self.text_box.configure(state="disabled")  # disable text box
            if not self.end_time:
                self.end_time = datetime.datetime.now()  # set user end time
            self.get_results(len(user_input), user_words)

    def get_results(self, chars, words):
        seconds = (self.end_time - self.start_time).total_seconds()
        wpm = int((chars / 5) / (seconds / 60))

        # count errors
        errors = 0
        for i, word in enumerate(self.phrase):
            if word != words[i]:
                errors += 1
        results = f"WPM: {wpm},  WORDS: {(chars / 5)},  WORDS WITH ERRORS: {errors}"
        result_label = Label(text=results, font=self.font, bg=self.color, fg="black")
        result_label.pack()
        self.text_box.unbind("<KeyRelease>")  # stop listening for typing
