# %%
#GUI with Exit button and Clear button
import tkinter as tk
from tkinter import filedialog
import main

root = tk.Tk()
root.title("GPA Calculator")
root.config(bg='#B2BEB5')
root.attributes('-fullscreen', True)



# Create title label
title_label = tk.Label(root, text="GPA Calculator", font=("Arial", 30), fg="black", bg="#B2BEB5")
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Create file directory box
dir_box = tk.Text(root, width=25, height=1)
dir_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Create browse button
browse_button = tk.Button(root, text="Browse", width=10)
browse_button.grid(row=2, column=0, sticky="w", padx=10)

# Create calculate button
calc_button = tk.Button(root, text="Calculate", width=10)
calc_button.grid(row=2, column=0, padx=10)

# Create clear button
clear_button = tk.Button(root, text="Clear", width=10)
clear_button.grid(row=2, column=0, padx=10, sticky="e")

# Create file contents box
file_box = tk.Text(root, height=10)
file_box.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Create calculation box
calc_box = tk.Text(root, height=5)
calc_box.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

# Create empty box
empty_box = tk.Frame(root, bg="white")
empty_box.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

# Create function to display file contents in file_box
def display_file_contents(file_path):
    dir_box.delete(1.0, tk.END) # Clear previous contents
    with open(file_path, "r") as file:
        file_contents = file.read()
        dir_box.insert(tk.END, file_path)
        file_box.delete(1.0, tk.END) # Clear previous contents
        file_box.insert(tk.END, file_contents)

# Function to handle file selection from directory browser
def select_file():
    file_path = filedialog.askopenfilename()
    display_file_contents(file_path)
    
# Function to clear text from all textboxes
def clear_text():
    dir_box.delete(1.0, tk.END)
    file_box.delete(1.0, tk.END)
    calc_box.delete(1.0, tk.END)

# Function to exit program
def exit_program():
    root.destroy()

# Attach select_file function to browse button
browse_button.config(command=select_file)

# Attach calculate function to calculate button
calc_button.config(command=lambda: calc_box.insert(tk.END, main.fetch(dir_box.get(1.0, tk.END))))
#calc_box.insert(tk.END, 3+4)
# Attach clear_text function to clear button
clear_button.config(command=clear_text)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=0, column=1, sticky="ne", padx=10, pady=(10, 0))

# Set grid weights to allow for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(3, weight=1)

root.mainloop()




# %%


# %%
