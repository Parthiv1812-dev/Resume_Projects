import random
from tkinter import *
import pandas
from pandas import DataFrame
BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
french_words = data.French.tolist()
english_words = data.English.tolist()
index = 0

def start():
    global french_words, english_words
    f_dict = {
        "French": french_words,
        "English": english_words
    }
    f_data = DataFrame(f_dict)
    f_data.to_csv("data/words_to_learn.csv", index=False)

def change_word_french():
    global index, flip_timer, french_words
    window.after_cancel(flip_timer)
    canvas.itemconfig(show_image, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    random_word = random.choice(french_words)
    index = french_words.index(random_word)
    canvas.itemconfig(word_text, text=random_word, fill="black")
    flip_timer = window.after(3000, change_word_english)

def change_word_english():
    global index, english_words
    canvas.itemconfig(show_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_words[index], fill="white")


def remove_known():
    global index, english_words, french_words
    english_words.pop(index)
    french_words.pop(index)
    final_dict = {
        "French": french_words,
        "English": english_words,
    }

    final_data = DataFrame(final_dict)
    final_data.to_csv("data/words_to_learn.csv", index=False)





# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_word_english)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,  highlightthickness=0)
show_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#buttons:
tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: [change_word_french(), remove_known()])
tick_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word_french)
cross_button.grid(row=1, column=0)

#Label:
# Language_label = Label(text="French", fg="black", font=("Ariel", 40, "italic"), bg="white", highlightthickness=0)
# Language_label.place(x=310, y=150)
#
# Word_label = Label(text="trouve", fg="black", font=("Ariel", 60, "bold"), bg="white", highlightthickness=0)
# Word_label.place(x=280, y=263)



change_word_french()


start()

window.mainloop()