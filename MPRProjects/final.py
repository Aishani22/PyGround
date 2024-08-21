import subprocess
from tkinter import *
from PIL import Image, ImageTk
from RockPaperScissors.main import *
from capitals import *
from LogosAndBrands.LogoGame import *


def click():
    print("I was clicked")


def snakeGame1():
    subprocess.Popen(["python", "day-20-start/main.py"])


def rpsGame1():
    GameStart()


def pingPongGame1():
    subprocess.Popen(["python", "day-22-start/main.py"])


def turtleCross():
    subprocess.Popen(["python", "turtle-crossing-start/main.py"])


def turtleRace1():
    subprocess.Popen(["python", "TurtleRace.py"])


def etchASketch1():
    subprocess.Popen(["python", "EtchASketch.py"])


def capitals1():
    subprocess.Popen(["python", "capitals.py"])


def logos():
    subprocess.Popen(["python", "LogosAndBrands/LogoGame.py"])


def hangman1():
    subprocess.Popen(["python", "Hangman/hangman.py"])


common_button_pad_x = 20
common_button_pad_y = 20
common_space_pad_x = 35
common_space_pad_y = 50

window = Tk()
window.geometry("1400x800")
window.resizable(False, False)
window.title("PyGround")
window.config(background="#232525")
pic = ImageTk.PhotoImage(Image.open("snake.png").resize((318, 318)))
icon = PhotoImage(file="Py.png")
window.iconphoto(True, icon)

main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
second_frame.config(background="#232525")

snake_pic = ImageTk.PhotoImage(Image.open("snake.png").resize((318, 318)))
rps_pic = ImageTk.PhotoImage(Image.open("rps.png").resize((318, 318)))
pingPong_pic = ImageTk.PhotoImage(Image.open("pingPong.png").resize((318, 318)))
turtleRoad_pic = ImageTk.PhotoImage(Image.open("turtleroad.png").resize((318, 318)))
turtleRace_pic = ImageTk.PhotoImage(Image.open("turtleRace.png").resize((318, 318)))
sketch_pic = ImageTk.PhotoImage(Image.open("sketch.png").resize((318, 318)))
capitals_pic = ImageTk.PhotoImage(Image.open("capitals.png").resize((318, 318)))
logos_pic = ImageTk.PhotoImage(Image.open("logos.png").resize((318, 318)))
hangman_pic = ImageTk.PhotoImage(Image.open("hangman.png").resize((318, 318)))

button1 = Button(second_frame,
                 text=" SNAKE GAME ",
                 command=snakeGame1,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=snake_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button1.grid(row=0, column=0, padx=2 * common_space_pad_x, pady=common_space_pad_y)

button2 = Button(second_frame,
                 text=" ROCK PAPER SCISSOR",
                 command=rpsGame1,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=rps_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button2.grid(row=0, column=1, padx=0, pady=common_space_pad_y)

button3 = Button(second_frame,
                 text="PING PONG",
                 command=pingPongGame1,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=pingPong_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button3.grid(row=0, column=2, padx=2 * common_space_pad_x, pady=common_space_pad_y)

button4 = Button(second_frame,
                 text="TURTLE CROSSING",
                 command=turtleCross,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=turtleRoad_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button4.grid(row=1, column=0, padx=2 * common_space_pad_x, pady=common_space_pad_y)

button5 = Button(second_frame,
                 text="TURTLE RACE",
                 command=turtleRace1,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=turtleRace_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button5.grid(row=1, column=1, padx=0, pady=common_space_pad_y)

button6 = Button(second_frame,
                 text="ETCH A SKETCH",
                 command=etchASketch1,
                 font=("Impact", 26),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=sketch_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button6.grid(row=1, column=2, padx=2 * common_space_pad_x, pady=common_space_pad_y)

button7 = Button(second_frame,
                 text="GUESS THE CAPITAL",
                 command=capitals1,
                 font=("Impact", 30),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=capitals_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button7.grid(row=2, column=0, padx=2 * common_space_pad_x, pady=common_space_pad_y)

button8 = Button(second_frame,
                 text="NAME THE LOGOS",
                 command=logos,
                 font=("Impact", 30),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=logos_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button8.grid(row=2, column=1, padx=0, pady=common_space_pad_y)

button9 = Button(second_frame,
                 text="HANGMAN",
                 command=hangman1,
                 font=("Impact", 30),
                 fg="#154040",
                 bg="#C7EFEF",
                 activebackground="#C7EFEF",
                 activeforeground="#154040",
                 state=ACTIVE,
                 image=hangman_pic,
                 compound='top',
                 padx=common_button_pad_x,
                 pady=common_button_pad_y
                 )
button9.grid(row=2, column=2, padx=2 * common_space_pad_x, pady=common_space_pad_y)

# button10 = Button(second_frame,
#                   text="Thanos Is Coming",
#                   command=click,
#                   font=("Impact", 30),
#                   fg="#154040",
#                   bg="#C7EFEF",
#                   activebackground="#C7EFEF",
#                   activeforeground="#154040",
#                   state=ACTIVE,
#                   image=pic,
#                   compound='top',
#                   padx=common_button_pad_x,
#                   pady=common_button_pad_y
#                   )
# button10.grid(row=3, column=0, padx=2 * common_space_pad_x, pady=common_space_pad_y)
#
# button11 = Button(second_frame,
#                   text="Thanos Is Coming",
#                   command=click,
#                   font=("Impact", 30),
#                   fg="#154040",
#                   bg="#C7EFEF",
#                   activebackground="#C7EFEF",
#                   activeforeground="#154040",
#                   state=ACTIVE,
#                   image=pic,
#                   compound='top',
#                   padx=common_button_pad_x,
#                   pady=common_button_pad_y
#                   )
# button11.grid(row=3, column=1, padx=0, pady=common_space_pad_y)
#
# button12 = Button(second_frame,
#                   text="Thanos Is Coming",
#                   command=click,
#                   font=("Impact", 30),
#                   fg="#154040",
#                   bg="#C7EFEF",
#                   activebackground="#C7EFEF",
#                   activeforeground="#154040",
#                   state=ACTIVE,
#                   image=pic,
#                   compound='top',
#                   padx=common_button_pad_x,
#                   pady=common_button_pad_y
#                   )
# button12.grid(row=3, column=2, padx=2 * common_space_pad_x, pady=2 * common_space_pad_y)

window.mainloop()
