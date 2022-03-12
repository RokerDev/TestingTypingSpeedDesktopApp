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

        self.lbl_description = ttk.Label(self, text="Test your typing skills:", font=("Courier", 45))
        self.lbl_description.grid(column=0, row=0, columnspan=3, pady=15)

        self.lbl_description1 = ttk.Label(self, text="Words per Minute: ", relief=tk.SUNKEN, font=("Courier", 15), width=20)
        self.lbl_description1.grid(column=0, row=1, pady=25)

        self.lbl_description2 = ttk.Label(self, text="Chars per Minute: ", relief=tk.SUNKEN, font=("Courier", 15), width=20)
        self.lbl_description2.grid(column=1, row=1,)

        self.lbl_description3 = ttk.Label(self, text="Misspells: ", relief=tk.SUNKEN, font=("Courier", 15), width=20)
        self.lbl_description3.grid(column=2, row=1,)

        self.frm_display = ttk.Frame(self, )
        self.frm_display.grid(column=0, row=2, columnspan=3, pady=15)
        self.lbl_display_list1 = ttk.Label(self.frm_display, relief=tk.SUNKEN, font=("Courier", 40),
                                           background="white", width=14)
        self.lbl_display_list1.pack(side=tk.LEFT, fill=tk.X)

        self.text_str_var = tk.StringVar()
        self.text_str_var.trace("w", self.user_test)

        self.ent_text = ttk.Entry(self.frm_display, font=("Courier", 40), textvariable=self.text_str_var, width=1, )
        self.ent_text.pack(side=tk.LEFT, )

        self.lbl_display_list = ttk.Label(self.frm_display, text="Cos", relief=tk.SUNKEN, font=("Courier", 40),
                                          background="white",
                                          width=15)
        self.lbl_display_list.pack(side=tk.RIGHT, fill=tk.X)

        # Backend
        self.words_list = self.load_words_list()
        self.generated_words_string = ""
        self.well_typed_side = "              "
        self.misspells = 0
        self.words_per_minute = 0
        self.chars_per_minute = 0
        for _ in range(6):
            self.generate_word()

        self.lbl_display_list["text"] = self.generated_words_string[1:]
        self.text_str_var.set(self.generated_words_string[0])
        self.ent_text.icursor(0)
        self.ent_text.focus_set()

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

    def user_test(self, *args):
        text = self.text_str_var.get()

        if len(text) == 2:

            # if user type proper letter then:
            if text[0] == text[1]:
                self.chars_per_minute += 1

                # add first letter from generated string to end of well typed side label text
                self.well_typed_side += self.generated_words_string[0]

                # set second letter from generated words at first place
                self.generated_words_string = self.generated_words_string[1:]

                # set on the right label the text of the generated word from second place
                self.lbl_display_list["text"] = self.generated_words_string[1:]

                # set next letter to type in entry widget
                self.text_str_var.set(self.generated_words_string[0])

                # set cursor before first place
                self.ent_text.icursor(0)

                # remove first letter from well type side label text
                self.well_typed_side = self.well_typed_side[1:]
                self.lbl_display_list1["text"] = self.well_typed_side

            # if user finish another word properly
            if text[0] == " " and text[1] == " ":
                self.words_per_minute += 1
                self.generate_word()

            # if user introduced wrong input
            else:

                # set the same letter to type in entry widget
                self.text_str_var.set(self.generated_words_string[0])

                # set cursor before letter
                self.ent_text.icursor(0)

                # add 1 to misspell counter
                self.misspells += 1

        print(f"WPM: {self.words_per_minute}. CPM: {self.chars_per_minute}.")


if __name__ == "__main__":
    app = TypeSpeedTest()
    app.mainloop()
