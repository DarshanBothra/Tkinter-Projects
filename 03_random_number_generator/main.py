from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
from tkinter import messagebox

root = Tk()
root.iconbitmap("icon.ico")
root.title("  Random Number Generator")

def generate():
    random_number_text_box.delete(0, END)
    try:

        first_number = first_number_text_box.get()
        last_number = last_number_text_box.get()

        first_number = int(first_number)
        last_number = int(last_number)

        if first_number > last_number:
            messagebox.showerror(title = "  Value Error", message = "First Number should be Smaller than Last Number")
            first_number_text_box.delete(0, END)
            last_number_text_box.delete(0, END)

            return # to break the function

        random_number = randint(first_number, last_number)
        random_number_text_box.insert(0, str(random_number))


    except Exception:
        first_number_text_box.delete(0, END)
        last_number_text_box.delete(0, END)
        messagebox.showerror(title = "  Value Error", message = "Enter an Integer Please!")



# Heading
heading_label = Label(root, text = "RANDOM NUMBER GENERATOR", font = ("Ubuntu Mono", 35, "bold"), anchor = CENTER, fg = "#525252")
heading_label.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 10)

# First Number
first_number_label = Label(root, text = "ENTER FIRST NUMBER:", font = ("Calibri", 18, "bold"))
first_number_label.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)

first_number_text_box = ttk.Entry(root, width = 20, font = ("Calibri", 18, "bold"))
first_number_text_box.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 5)

# Second Number
last_number_label = Label(root, text = "ENTER FINAL NUMBER:", font = ("Calibri", 18, "bold"))
last_number_label.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)

last_number_text_box = ttk.Entry(root, width = 20, font = ("Calibri", 18, "bold"))
last_number_text_box.grid(row = 2, column = 1, sticky = E, padx = 10, pady = 5)

# Random Number Choosing Button
random_btn = ttk.Button(root, command = generate, text = "GENERATE RANDOM NUMBER", style = "randBtn.TButton", width = 45)
random_btn.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 5)
ttk.Style().configure('randBtn.TButton', font=("Calibri", 18))

# Random Number
random_number_label = Label(root, text = "YOUR RANDOM NUMBER:", font = ("Calibri", 18, "bold"))
random_number_label.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 5)

random_number_text_box = ttk.Entry(root, width = 20, font = ("Calibri", 18, "bold"))
random_number_text_box.grid(row = 4, column = 1, sticky = E, padx = 10, pady = 5)

root.mainloop()