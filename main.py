import random
import tkinter as tk
from tkinter import ttk, messagebox


class TypeSpeedTest(tk.Tk):

    def __init__(self):
        super().__init__()

        # GUI part
        self.title("Type Speed Test Desktop Application")
        self.geometry(f"{int(self.winfo_screenwidth() / 2)}x{int(self.winfo_screenheight() / 4)}")

        self.lbl_description = ttk.Label(self, text="Test your typing skills:", font=("Courier", 45))
        self.lbl_description.grid(column=0, row=0, columnspan=3, pady=10)

        self.lbl_timer = ttk.Label(self, text="00:01:00", font=("Courier", 25))
        self.lbl_timer.grid(column=0, row=1, columnspan=3, pady=10)

        self.lbl_wpm = ttk.Label(self, text="Words per Minute: ", relief=tk.SUNKEN, font=("Courier", 15), width=23)
        self.lbl_wpm.grid(column=0, row=2, pady=10)

        self.lbl_cpm = ttk.Label(self, text="Chars per Minute: ", relief=tk.SUNKEN, font=("Courier", 15), width=23)
        self.lbl_cpm.grid(column=1, row=2, )

        self.lbl_mpm = ttk.Label(self, text="Misspells: ", relief=tk.SUNKEN, font=("Courier", 15), width=23)
        self.lbl_mpm.grid(column=2, row=2, )

        self.frm_display = ttk.Frame(self, )
        self.frm_display.grid(column=0, row=3, columnspan=3, pady=10)
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
        self.ask = True
        self.time = 60
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

    def update_clock(self):
        hours = str(self.time // 3600)
        hours = hours.rjust(2, "0")
        minutes, seconds = (str(self.time // 60), str(self.time % 60))
        minutes = minutes.rjust(2, "0")
        seconds = seconds.rjust(2, "0")
        self.lbl_timer["text"] = f"{hours}:{minutes}:{seconds}"
        print(hours, minutes, seconds)
        self.time -= 1
        end = self.after(1000, self.update_clock)
        if self.time < 0:
            self.after_cancel(end)
            self.ent_text.config(state=tk.DISABLED)
            self.try_again()

    def try_again(self):
        end_message = f"""
                        Words per minute: {self.words_per_minute}
                        Chars per minute: {self.chars_per_minute}
                    Misspells per minute: {self.misspells}
                    """
        self.ask = messagebox.askyesno("Want to try again?", end_message)
        print(self.ask)
        if not self.ask:
            self.destroy()
        else:
            self.well_typed_side = "              "
            self.generated_words_string = ""
            self.ask = "yes"
            self.lbl_timer["text"] = "00:01:00"
            self.time = 60
            self.words_per_minute = 0
            self.lbl_wpm["text"] = f"Words per Minute: {self.words_per_minute}"
            self.chars_per_minute = 0
            self.lbl_cpm["text"] = f"Chars per Minute: {self.chars_per_minute}"
            self.misspells = 0
            self.lbl_mpm["text"] = f"Misspells: {self.misspells}"
            for _ in range(6):
                self.generate_word()

            self.lbl_display_list["text"] = self.generated_words_string[1:]
            self.lbl_display_list1["text"] = self.well_typed_side
            self.ent_text.config(state=tk.NORMAL)
            self.text_str_var.set(self.generated_words_string[0])
            self.ent_text.icursor(0)
            self.ent_text.focus_set()

    def user_test(self, *args):
        text = self.text_str_var.get()

        if len(text) == 2:
            if self.time == 60:
                self.update_clock()

            # if user type proper letter then:
            if text[0] == text[1]:
                self.chars_per_minute += 1
                self.lbl_cpm["text"] = f"Chars per Minute: {self.chars_per_minute}"

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
                self.lbl_wpm["text"] = f"Words per Minute: {self.words_per_minute}"
                self.generate_word()

            # if user introduced wrong input
            if text[0] != text[1]:
                # set the same letter to type in entry widget
                self.text_str_var.set(self.generated_words_string[0])

                # set cursor before letter
                self.ent_text.icursor(0)

                # add 1 to misspell counter
                self.misspells += 1
                self.lbl_mpm["text"] = f"Misspells: {self.misspells}"

        print(f"WPM: {self.words_per_minute}. CPM: {self.chars_per_minute}.")


if __name__ == "__main__":
    app = TypeSpeedTest()
    app.mainloop()
