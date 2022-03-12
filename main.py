import random
import tkinter as tk
from tkinter import ttk


# To do list:
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

        self.lbl_display_list = ttk.Label(self, text="Cos", relief=tk.SUNKEN, font=("Courier", 40))
        self.lbl_display_list.grid(column=0, row=0, padx=20, pady=10, sticky=tk.EW)
        self.columnconfigure(0, minsize=100, weight=1)
        self.rowconfigure(0, minsize=80, weight=1)

        self.text_str_var = tk.StringVar()
        self.text_str_var.trace("w", self.get_user_entry)

        self.ent_text = ttk.Entry(self, font=("Courier", 40), textvariable=self.text_str_var, )
        self.ent_text.grid(column=0, row=1, padx=20, pady=10, sticky=tk.EW)
        self.rowconfigure(1, minsize=60, weight=1, )

        # Backend
        self.words_list = self.load_words_list()
        self.generated_words_string = ""
        self.words_per_minute = 0
        self.chars_per_minute = 0
        for _ in range(6):
            self.generate_word()

        self.lbl_display_list.config(text=self.generated_words_string)

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

    def get_user_entry(self, *args):
        text = self.text_str_var.get()

        if text != self.generated_words_string[:len(text)]:
            self.text_str_var.set(text[:-1])
        else:
            self.chars_per_minute += 1
            if text.endswith(" "):
                self.generate_word()
                self.generated_words_string = self.generated_words_string[len(text):]
                self.lbl_display_list["text"] = self.generated_words_string
                self.text_str_var.set("")
                self.words_per_minute += 1

        print(f"WPM: {self.words_per_minute}. CPM: {self.chars_per_minute}.")



if __name__ == "__main__":
    app = TypeSpeedTest()
    app.mainloop()
