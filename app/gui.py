import tkinter as tk
from tkinter import ttk
from threading import Thread

from app.scientist import Scientist
from app.database import Database
from app.pyhas import exec_haskell

class App:
    def __init__(self, master=None):
        # build ui
        self.main = tk.Tk() if master is None else tk.Toplevel(master)
        self.top = ttk.Frame(self.main)

        self.top.pack(side='top')
        self.middle = ttk.Frame(self.main)

        self.middle.configure(relief='flat', takefocus=False)
        self.middle.pack(side='top')

        self.bottom = ttk.Frame(self.main)

        self.forms = ttk.Frame(self.bottom)
        self.forms.pack(side='top')

        self.output = ttk.Frame(self.bottom)
        self.output.pack(side='top')

        self.bottom.pack(side='top')
        self.main.minsize(500, 500)

        # Main widget
        self.mainwindow = self.main
        self.mainwindow.title("Pyhas Erdos")

        self.label_form = ttk.Label(self.forms, text="Target scientist name")
        self.label_form.pack()
        self.entry_form = ttk.Entry(self.forms)
        self.entry_form.pack()

        self.button_form = ttk.Button(self.forms, text="Calc!", command=self.calc)
        self.button_form.pack()

        self.db = Database("./db.json")
        self.db.open()

    def run(self):
        self.mainwindow.mainloop()

    def calc(self):
        self.clear_frame(self.output)

        name = self.entry_form.get()
        scientist = Scientist(name)
        if not scientist:
            self.txt = ttk.Label(self.output, text="Enter UID!!")
            self.txt.pack(side='top')
            return

        self.button_form['state'] = tk.DISABLED

        sc_str = '(' + scientist.to_str() + ')'
        self.res = []
        thread_rest = Thread(target=exec_haskell, args=(self.db.to_str(), sc_str, self.res, ))
        thread_rest.start()
        self.monitor(thread_rest, self.render_output, self.res)

    def render_output(self):
        print(self.res)
        if self.res[0] == "error":
            self.txt = ttk.Label(self.output, text="Error")
            self.txt.pack(side='top')
            return
        else:
            result = "Erdos number is : " + self.res[0]
            self.txt = ttk.Label(self.output, text=result)
            self.txt.pack(side='top')

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def monitor(self, thread_rest, render_output, res):
        if thread_rest.is_alive():
            self.main.after(100, lambda: self.monitor(thread_rest, render_output, res))
        else:
            self.button_form['state'] = tk.NORMAL
            self.render_output()