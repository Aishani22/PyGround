from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window = Tk()
window.title("Hangman")
window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

word_list = ["LION", "PANDA", "TIGER", "DOG", "CAT", "RABIT", "MOUSE", "ELEPHANT", "DEER", "WOLF",
             "JAGUAR", "PUMA", "GOAT", "HORSE", "PANTHER",
             "CHEETAH", "LEOPARD", "MONKEY", "COW", "BULL", "KANGAROO", "GIRAFFE", "FOX", "BEAR", "GORILLA", "DONKEY",
             "ANTELOPE", "ZEBRA", "KOALA"]

photos = [PhotoImage(file="Hangman/hang0.png"), PhotoImage(file="Hangman/hang1.png"),
          PhotoImage(file="Hangman/hang2.png"),
          PhotoImage(file="Hangman/hang3.png"),
          PhotoImage(file="Hangman/hang4.png"), PhotoImage(file="Hangman/hang5.png"),
          PhotoImage(file="Hangman/hang6.png"),
          PhotoImage(file="Hangman/hang7.png"),
          PhotoImage(file="Hangman/hang8.png"), PhotoImage(file="Hangman/hang9.png"),
          PhotoImage(file="Hangman/hang10.png"), PhotoImage(file="Hangman/hang11.png")]


def newGame():
    messagebox.showinfo("Instruction", "It's an Animal Name")
    the_word = random.choice(word_list)
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image=photos[0])
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(" ".join("_" * len(the_word)))


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "Congratulations! You Guessed it!")
                    newGame()
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over!")
                messagebox.showinfo("Hangman", "The correct answer is " + "".join(the_word_withSpaces.split()))


imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n = 0


def create_button_command(char):
    return lambda: guess(char)


for c in ascii_uppercase:
    button_command = create_button_command(c)
    Button(window, text=c, command=button_command, font=("Helvetica 18"), width=4).grid(row=1 + n // 9, column=n % 9)
    n += 1

Button(window, text="new\nGame", command=lambda: newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8,
                                                                                             sticky="NSWE")

newGame()
window.mainloop()
