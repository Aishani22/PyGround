import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

brand_image_mapping = {
    "LogosAndBrands/Logos/Adidas.png": "Adidas",
    "LogosAndBrands/Logos/AirJordan.png": "Air Jordan",
    "LogosAndBrands/Logos/Amazon.png": "Amazon",
    "LogosAndBrands/Logos/Android.png": "Android",
    "LogosAndBrands/Logos/Barbie.png": "Barbie",
    "LogosAndBrands/Logos/Bmw.png": "BMW",
    "LogosAndBrands/Logos/BurgerKing.png": "Burger King",
    "LogosAndBrands/Logos/CalvinKlein.png": "Calvin Klein",
    "LogosAndBrands/Logos/CocaCola.png": "Coca Cola",
    "LogosAndBrands/Logos/Facebook.png": "Facebook",
    "LogosAndBrands/Logos/Levis.png": "Levis",
    "LogosAndBrands/Logos/MasterCard.png": "Mastercard",
    "LogosAndBrands/Logos/Monster.png": "Monster",
    "LogosAndBrands/Logos/Mercedes.png": "Mercedes",
    "LogosAndBrands/Logos/Mtv.png": "Mtv",
    "LogosAndBrands/Logos/Netflix.png": "Netflix",
    "LogosAndBrands/Logos/Nike.png": "Nike",
    "LogosAndBrands/Logos/Pringles.png": "Pringles",
    "LogosAndBrands/Logos/Redbull.png": "Redbull",
    "LogosAndBrands/Logos/Sony.png": "Sony",
    "LogosAndBrands/Logos/Starbucks.png": "Starbucks",
    "LogosAndBrands/Logos/Twitter.png": "Twitter",
    "LogosAndBrands/Logos/Youtube.png": "Youtube"
}


class GameWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Brand Logo Guessing Game")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the width and height of the window
        window_width = 500
        window_height = 500

        # Calculate the x and y coordinates for the window to be centered
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.configure(bg="#A5DD9B")
        self.resizable(False, False)

        self.score = 0
        self.asked_questions = set()
        self.create_widgets()
        self.next_question()
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('Bootstrap.TButton', font=('Cambria', 16), background="#508D69", foreground="black")

    def create_widgets(self):
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.answer_entry = ttk.Entry(self)
        self.answer_entry.pack(pady=5)

        self.submit_button = ttk.Button(self, text="Submit", command=self.check_answer, style='Bootstrap.TButton')
        self.submit_button.pack(pady=5)

        self.result_label = ttk.Label(self, text="Good Luck", foreground="blue", font=('Cambria', 12))
        self.result_label.pack(pady=10)

        self.score_label = ttk.Label(self, text=f"Score: {self.score}", font=('Cambria', 16))
        self.score_label.pack(pady=5)

    def load_and_resize_image(self, image_path):
        original_image = Image.open(image_path)
        original_width, original_height = original_image.size
        resized_image = original_image.resize((original_width // 2, original_height // 2))
        return ImageTk.PhotoImage(resized_image)

    def next_question(self):
        remaining_questions = [q for q in brand_image_mapping.keys() if q not in self.asked_questions]
        if remaining_questions:
            self.image_path = random.choice(remaining_questions)
            self.brand_name = brand_image_mapping[self.image_path].lower()
            self.brand_image = self.load_and_resize_image(self.image_path)
            self.image_label.config(image=self.brand_image)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("You Won", "Congratulations! You've guessed all the logos!")
            self.destroy()
            self.parent.deiconify()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == self.brand_name:
            self.score += 1
            self.result_label.config(text="Correct!", font=('Cambria', 14), foreground="green")
            self.score_label.config(text=f"Score: {self.score}")
            self.asked_questions.add(self.image_path)
            self.after(1200, self.next_question)
        else:
            self.result_label.config(text=f"The correct answer is {self.brand_name.upper()}", font=('Cambria', 14), foreground="red", justify="center")
            messagebox.showerror("Wrong", "Sorry, that's incorrect.")
            self.destroy()
            self.parent.deiconify()


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brand Logo Guessing Game")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the width and height of the window
        window_width = 500
        window_height = 500

        # Calculate the x and y coordinates for the window to be centered
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.configure(bg="#A5DD9B")
        self.resizable(False, False)

        intro_image = Image.open("panda.png")
        intro_image = intro_image.resize((200, 200))
        self.intro_image = ImageTk.PhotoImage(intro_image)
        self.intro_label = tk.Label(self, image=self.intro_image)
        self.intro_label.pack(pady=30)

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TLabel', font=('Cambria', 16))
        style.configure('Bootstrap.TButton', font=('Cambria', 16), background="#508D69", foreground="black")

        self.start_button = ttk.Button(self, text="Start a New Game", command=self.start_new_game,
                                       style='Bootstrap.TButton')
        self.start_button.pack(pady=20)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit, style='Bootstrap.TButton')
        self.quit_button.pack(pady=20)

    def start_new_game(self):
        self.withdraw()
        self.game_window = GameWindow(self)


def startLogosGame():
    if __name__ == "__main__":
        app = GameApp()
        app.mainloop()


startLogosGame()
