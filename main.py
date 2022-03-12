import tkinter as tk
from tkinter import ttk


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


if __name__ == "__main__":
    app = TypeSpeedTest()
    app.mainloop()
