from tkinter import *
from TypingTest import TypingTest
import time

#Constants
APP_NAME = "Typing Speed Test"
NUMBER_OF_WORDS = 20
PHRASE_FONT = ("Arial", 24, "bold")

# initialize the typing speed test class
test = TypingTest()
test.open_window(APP_NAME)  # creates tkinter window
test.get_phrase()           # gets random words to create a phrase
test.build_phrase_labels(NUMBER_OF_WORDS, PHRASE_FONT)
test.create_text_box(PHRASE_FONT)

# TODO: UI setup show results

# TODO: Compare current word typed with current word displayed & Show errors (RED CHARACTERS)
test.text_box.bind("<KeyRelease>", test.get_text_input)

# TODO: Track time from start of typing to end of test.

# TODO: Calculate CPM, WPM, & Accuracy


# keep UI Open
test.window.mainloop()
