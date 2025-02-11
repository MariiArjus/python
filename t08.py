import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
    else:
        dir_label.config(text="Kausta ei valitud.")

def save_directory():
    pass

aken = tk.Tk()
aken.title("pildi suuruse muutmine")
aken.geometry("450x400")


label = tk.Label(aken, text = "Pildi suurus 200x200", font= "Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height = 10, width = 50)
inputtxt.pack(pady = 10)

open_button = tk.Button(aken, text="salvesta pildid", command=save_directory)
open_button.pack(pady = 10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()