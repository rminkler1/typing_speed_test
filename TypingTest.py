import random
from tkinter import *
import tkinter.ttk as ttk


class TypingTest:
    def __init__(self):
        self.phrase = []    # store the randomly selected words here
        self.phrase_labels = []     # store tkinter labels for each word here
        self.window = Tk()
        self.text_box = None

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
        self.window.config(padx=20, pady=20)

    def build_phrase_labels(self, num, font):
        # iterate through all words
        for i, word in enumerate(self.phrase):
            if i % 5 == 0:  # every fifth word starting at 0, create a frame
                if i > 0:   # close the previous frame before opening a new one
                    phrase_frame.pack()
                phrase_frame = Frame(self.window, pady=5)

            # build the labels for tkinter. store them in a list to reference later
            self.phrase_labels.append(Label(phrase_frame, text=word, font=font))
            self.phrase_labels[i].pack(side="left")

            if i == num - 1:    # close the last frame
                phrase_frame.pack()

    def create_text_box(self, font):
        # UI setup input box for text input
        self.text_box = Text(height=5, width=50, font=font, wrap=WORD)
        self.text_box.focus()
        self.text_box.config(pady=20, padx=20)
        self.text_box.pack(pady=30)
