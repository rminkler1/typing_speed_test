from TypingTest import TypingTest

#Constants
APP_NAME = "Typing Speed Test"
NUMBER_OF_WORDS = 20
PHRASE_FONT = ("Arial", 30, "bold")
BG_COLOR = "#a1b6d5"

# initialize the typing speed test class
test = TypingTest(NUMBER_OF_WORDS, PHRASE_FONT, BG_COLOR)
test.open_window(APP_NAME)  # creates tkinter window
test.get_phrase()           # gets random words to create a phrase
test.build_phrase_labels()
test.create_text_box()

# Run on each character entered in the text box.
test.text_box.bind("<KeyRelease>", test.check_user_input)

# keep UI Open
test.window.mainloop()
