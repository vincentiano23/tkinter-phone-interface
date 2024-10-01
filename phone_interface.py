import tkinter as tk
from tkinter import messagebox

# Function to display the button click on the phone screen
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to simulate a call
def make_call():
    number = entry.get()
    if number:
        messagebox.showinfo("Calling", f"Calling {number}...")
    else:
        messagebox.showwarning("Error", "Enter a number to call")

# Setting up the main window
root = tk.Tk()
root.title("Phone Interface")

# Creating the display
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Creating the buttons
button_texts = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]

buttons = []

# Creating and placing buttons in the grid
for i, text in enumerate(button_texts):
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda text=text: button_click(text))
    buttons.append(button)
    button.grid(row=(i // 3) + 1, column=i % 3)

# Adding additional functional buttons: Call and Clear
call_button = tk.Button(root, text="Call", padx=20, pady=20, font=('Arial', 14), bg='lightgreen', command=make_call)
call_button.grid(row=5, column=0, columnspan=2)

clear_button = tk.Button(root, text="Clear", padx=20, pady=20, font=('Arial', 14), bg='red', command=clear_display)
clear_button.grid(row=5, column=2)

# Running the main loop
root.mainloop()
