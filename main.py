"""
Purpose: Create a GUI flash cards app that can display information pairs from a CSV file
Tools: Pandas, Tkinter
"""
from tkinter import *
import pandas as pd
from pandas.errors import EmptyDataError
import random as r

#Pick BG Color
BACKGROUND_COLOR = "#B1DDC6"
current_word = ""

#New flashcards either from the words_to_learn list or the word list if it's the 1st program run
#Read the CSVs in as dictionaries
try:
    data = pd.DataFrame.to_dict(pd.read_csv("words_to_learn.csv"), orient="records")
except EmptyDataError:
    data = pd.DataFrame.to_dict(pd.read_csv("data/french_words.csv"), orient="records")


#Generate a new flashcard
def generate_card(correct):
    global current_word
    #If correct, remove the pair from the dict, convert it to a DataFrame and update the words_to_learn CSV
    if correct:
        data.remove(current_word)
        new_data = pd.DataFrame(data)
        new_data.to_csv("words_to_learn.csv", index=False)

    #Reset back to the front card
    canvas.itemconfig(image, image=front_img)
    canvas.itemconfig(language, text="French", fill="black")

    #Randomly pick a pair, display the front word, and wait 3s to flip the card
    current_word = r.choice(data)
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    window.after(3000, flip, current_word)


#Flip to the back card and word
def flip(current_word):
    canvas.itemconfig(image, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")

#UI Setup
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx= 50, pady=50)

back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Click To Start", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2,row=0)

#Correctly generate the next flashcard
y_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR,
                  command=lambda: generate_card(True))
y_button.grid(column=1, row=1)
x_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR,
                  command=lambda: generate_card(False))
x_button.grid(column=0, row=1)

#Start the game
generate_card(False)


window.mainloop()
