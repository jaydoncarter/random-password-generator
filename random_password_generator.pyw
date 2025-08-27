import random
import string
import tkinter
from tkinter import *

# -- Generation Logic -- #
def generate_password(length: int, capital: bool, number: bool, special: bool) -> str: # generates the password using
# certain randomly generated
    # ASCII characters
    # determines which characters can be part of the password
    characters = string.ascii_lowercase
    if capital:
        characters += string.ascii_uppercase
    if number:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = []

    # at least one of each selected character type
    if capital:
        password.append(random.choice(string.ascii_uppercase))
    if number:
        password.append(random.choice(string.digits))
    if special:
        password.append(random.choice(string.punctuation))

    # fills in the rest of the password to the desired length
    for i in range(length - len(password)):
        password.append(random.choice(characters))

    # reorders the values in the password list
    random.shuffle(password)
    # returns the list as one string
    return "".join(password)

def on_generate():
    # Sets generation parameters based on UI input
    length = int(length_slider.get())
    capital = var_capital.get()
    number = var_number.get()
    special = var_special.get()

    # Calls password generation function and displays it to the UI
    password = generate_password(length, capital, number, special)
    password_output.config(state="normal")
    password_output.delete(0, tkinter.END)
    password_output.insert(0, password)
    password_output.config(state="readonly")

    copy_button.config(text="Copy")

def copy_password():
    password = password_output.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        copy_button.config(text="Copied!")

# -- UI Setup -- #
# Window
root = tkinter.Tk()
root.title("Random Password Generator")
root.geometry("440x360")
root.minsize(440, 360)
root.configure(bg="black")
root.iconbitmap("logo.ico")

# Title
title_label = tkinter.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), fg="white", bg="black")
title_label.pack(pady=10, expand=True, anchor="s")

# Length Slider
length_frame = tkinter.Frame(root, bg="black")
length_frame.pack(pady=5)
tkinter.Label(length_frame, text="Password Length", fg="white", bg="black").pack(side="top")
length_slider = tkinter.Scale(length_frame, from_=4, to=32, orient=HORIZONTAL, fg="white", bg="black")
length_slider.set(12)
length_slider.pack()

# Generation Parameters
var_capital = tkinter.BooleanVar(value=False)
var_number = tkinter.BooleanVar(value=False)
var_special = tkinter.BooleanVar(value=False)

options_frame = tkinter.Frame(root, bg="black")
options_frame.pack(pady=5)

tkinter.Checkbutton(options_frame,
                    text="Include Uppercase",
                    variable=var_capital,
                    bg="black",
                    fg="white",
                    selectcolor="black").pack(anchor="w")
tkinter.Checkbutton(options_frame,
                    text="Include Numbers",
                    variable=var_number,
                    bg="black",
                    fg="white",
                    selectcolor="black").pack(anchor="w")
tkinter.Checkbutton(options_frame,
                    text="Include Special Characters",
                    variable=var_special,
                    bg="black",
                    fg="white",
                    selectcolor="black").pack(anchor="w")

# Generate button
generate_button = tkinter.Button(root,
                                 text="Generate Password",
                                 command=on_generate,
                                 font=("Arial", 12, "bold"),
                                 bg="blue",
                                 fg="white")
generate_button.pack(pady=10)

# Output field
password_output = tkinter.Entry(root, width=40, font=("Courier", 12), justify="center")
password_output.pack(pady=10)
password_output.config(state="readonly")

# Copy button
copy_button = tkinter.Button(root,
                                 text="Copy",
                                 command=copy_password,
                                 bg="gray",
                                 fg="white")
copy_button.pack(expand=True, anchor="n")

# Run the app
root.mainloop()