from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

#STEP 4: SAVE YOUR PROGRESS
def correct():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    data_dict.remove(current_card)
    words_to_learn_df = pd.DataFrame(data_dict)
    words_to_learn_df.to_csv("data/words_to_learn.csv",mode="w", index=False)

    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip)


#STEP 2 CONT.
def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip)

#STEP 3: FLIP THE CARDS
def flip():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

#STEP 1: CREATE THE UI WITH TKINTER
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#Canvas
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")

canvas.grid(row=0, column=0, columnspan=2)

#Canvas Text
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

#Buttons
tick_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

right = Button(image=tick_image, highlightthickness=0, command=correct)
left = Button(image=cross_image, highlightthickness=0, command=next_word)

right.grid(row=1, column=1)
left.grid(row=1, column=0)

#STEP 3 CONT.
flip_timer = window.after(3000, func=flip)

#STEP 2: CREATE NEW FLASH CARDS
#STEP 4 CONT.
try:
    data_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pd.read_csv("data/french_words.csv")
    data_dict = data_df.to_dict(orient="records")
else:
    data_dict = data_df.to_dict(orient="records")
next_word()

window.mainloop()