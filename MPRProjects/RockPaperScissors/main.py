from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk
import random
from tkinter import messagebox

def GameStart():
    class RockPaperScissors:

        def __init__(self, root):
            self.root = root
            self.root.title("Rock Paper Scissors")
            self.root.configure(background="#504099")
            self.create_buttons()

            self.rock = ImageTk.PhotoImage(Image.open("RockPaperScissors/rock.png").resize((318, 318)))
            self.paper = ImageTk.PhotoImage(Image.open("RockPaperScissors/paper.png").resize((318, 318)))
            self.scissors = ImageTk.PhotoImage(Image.open("RockPaperScissors/scissors.png").resize((318, 318)))
            self.rock_user = ImageTk.PhotoImage(Image.open("RockPaperScissors/rock_user.png").resize((318, 318)))
            self.paper_user = ImageTk.PhotoImage(Image.open("RockPaperScissors/paper_user.png").resize((318, 318)))
            self.scissors_user = ImageTk.PhotoImage(Image.open("RockPaperScissors/scissors_user.png").resize((318, 318)))

            # insert images
            self.user_label = Label(root, image=self.rock_user, bg="#504099")
            self.comp_label = Label(root, image=self.rock, bg="#504099")
            self.comp_label.grid(row=1, column=0)
            self.user_label.grid(row=1, column=4)

            # scores
            self.user_score = Label(root, text=0, font=("Arial", 28), bg="#504099", fg="white")
            self.comp_score = Label(root, text=0, font=("Arial", 28), bg="#504099", fg="white")
            self.comp_score.grid(row=1, column=1)
            self.user_score.grid(row=1, column=3)

            # indicators
            self.user_indicator = Label(root, font=("Cambria", 26), text="USER", bg="#504099", fg="white").grid(row=0,
                                                                                                                column=3)
            self.comp_indicator = Label(root, font=("Cambria", 26), text="COMPUTER", bg="#504099", fg="white").grid(
                row=0,
                column=1)

            # messages
            self.message = Label(root, text="", font=50, bg="#504099", fg="white")
            self.message.grid(row=3, column=2)



        # update message
        def updateMessage(self, x):
            self.message["text"] = x

        # update user score
        def updateUserScore(self):
            score = int(self.user_score["text"])
            score += 1
            self.user_score["text"] = str(score)

        # update comp score
        def updateCompScore(self):
            score = int(self.comp_score["text"])
            score += 1
            self.comp_score["text"] = str(score)

        # check winner
        def checkWinner(self, user, comp):
            if user == comp:
                self.updateMessage("IT'S A DRAW!")
            elif user == "rock":
                if comp == "paper":
                    self.updateMessage("YOU LOOSE!")
                    self.updateCompScore()
                else:
                    self.updateMessage("YOU WIN!")
                    self.updateUserScore()
            elif user == "paper":
                if comp == "scissors":
                    self.updateMessage("YOU LOOSE!")
                    self.updateCompScore()
                else:
                    self.updateMessage("YOU WIN!")
                    self.updateUserScore()
            elif user == "scissors":
                if comp == "rock":
                    self.updateMessage("YOU LOOSE!")
                    self.updateCompScore()
                else:
                    self.updateMessage("YOU WIN!")
                    self.updateUserScore()

        choices = ["rock", "paper", "scissors"]

        # update choices
        def updateChoice(self, x):
            # for computer
            comp_choice = random.choice(self.choices)
            if comp_choice == "rock":
                self.comp_label.configure(image=self.rock)
            elif comp_choice == "paper":
                self.comp_label.configure(image=self.paper)
            else:
                self.comp_label.configure(image=self.scissors)

            # for user
            if x == "rock":
                self.user_label.configure(image=self.rock_user)
            elif x == "paper":
                self.user_label.configure(image=self.paper_user)
            else:
                self.user_label.configure(image=self.scissors_user)

            self.checkWinner(x, comp_choice)

        def create_buttons(self):
            self.rockB = Button(self.root, width=20, height=2, text="ROCK", font=("Cambria", 12), bg="#FF7ED4",
                                fg="black",
                                command=lambda: self.updateChoice("rock"))
            self.rockB.grid(row=2, column=1)

            self.paperB = Button(self.root, width=20, height=2, text="PAPER", font=("Cambria", 12), bg="#50C4ED",
                                 fg="black",
                                 command=lambda: self.updateChoice("paper"))
            self.paperB.grid(row=2, column=2)

            self.scissorsB = Button(self.root, width=20, height=2, text="SCISSORS", font=("Cambria", 12), bg="#F5DD61",
                                    fg="black",
                                    command=lambda: self.updateChoice("scissors"))
            self.scissorsB.grid(row=2, column=3)

    messagebox.showinfo("Instructions", "1. SCISSOR beats PAPER.\n\n2. PAPER beats ROCK.\n\n3. ROCK beats SCISSOR.")
    root = Toplevel()
    app = RockPaperScissors(root)
    root.resizable(False, False)
    root.mainloop()
