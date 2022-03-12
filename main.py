import random
import tkinter as tk
from tkinter import ttk


# To do list:
# TODO: add text generator
# TODO: display generated text on label
# TODO: get user input
# TODO: check user input with generated text
# TODO: if correctly typed word then delete it and add + 1 to wpm variable
# TODO: add timer on GUI
# TODO: add function displaying user's results
# TODO: add function say hello to user

class TypeSpeedTest(tk.Tk):

    def __init__(self):
        super().__init__()

        # GUI part
        self.title("Type Speed Test Desktop Application")
        self.geometry(f"{int(self.winfo_screenwidth() / 2)}x{int(self.winfo_screenheight() / 4)}")

        self.lbl_display_list = ttk.Label(self, text="Cos", relief=tk.SUNKEN, font=("Courier", 60))
        self.lbl_display_list.grid(column=0, row=0, padx=20, pady=10, sticky=tk.EW)
        self.columnconfigure(0, minsize=100, weight=1)
        self.rowconfigure(0, minsize=80, weight=1)

        self.ent_text = ttk.Entry(self, font=("Courier", 40))
        self.ent_text.grid(column=0, row=1, padx=20, pady=10, sticky=tk.EW)
        self.rowconfigure(1, minsize=60, weight=1, )

        # Backend
        self.words_list = self.load_words_list()
        self.generated_words_string = ""
        self.generate_world()
        self.generate_world()
        self.generate_world()

    @staticmethod
    def load_words_list():
        with open("words-list.txt", mode="r") as words_list:
            temp_list = words_list.readline()
            return temp_list.split(",")

    def generate_word(self):
        generated_word = random.choice(self.words_list)
        if self.generated_words_string == "":
            self.generated_words_string += generated_word
        else:
            self.generated_words_string += f" {generated_word}"


if __name__ == "__main__":
    app = TypeSpeedTest()
    app.mainloop()
