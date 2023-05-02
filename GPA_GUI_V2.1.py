#!/usr/bin/env python
# coding: utf-8

# In[29]:


# USE

#__________________________________________________________TITLES_________________________________________________________#

import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import main

root = tk.Tk()
root.title("GPA Calculator")
root.config(bg='#CACBD1')
root.attributes('-fullscreen', True)

# ROGER WILLIAMS LABEL
title_label = ttk.Label(root, text="   Roger Williams", font=("Times New Roman", 20), foreground="white", background="#1E3261")
title_label.grid(row=1, column=0, columnspan=5, pady=(10, 0), sticky="nsew")

# UNIVERSITY LABEL
univ_label = ttk.Label(root, text="  University", font=("Times New Roman", 27), foreground="#60ADF0", background="#1E3261")
univ_label.grid(row=2, column=0, columnspan=5, pady=(0, 45), sticky="nsew")


#__________________________________________________________TEXTBOXES______________________________________________________#

# TOP SPACER BOX
top_space = tk.Entry(root, width=500, bg="#1E3261", fg="#1E3261", bd=0)
top_space = top_space.grid(row=0, rowspan=2, columnspan=5, pady=(0,30) , column=0, sticky="nesw")

# FILE DIRECTORY BOX
dir_box = tk.Entry(root, width=80, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
dir_box.insert(0, " Enter file path")
dir_box.bind("<FocusIn>", lambda event: dir_box.delete(0, tk.END))
dir_box.grid(row=3, column=0, padx=20, pady=10, sticky="w")

# FILE CONTENTS BOX
file_box = tk.Text(root, height=12, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
file_box.insert(tk.END, ' File contents will be displayed here.\n\n If entering manually, use the following format (include quotations):\n\n "Last","First","Student ID","Grade"')
file_box.bind("<FocusIn>", lambda event: file_box.delete(1.0, tk.END))
file_box.grid(row=5, column=0, padx=20, pady=30, sticky="w", columnspan=2)

# CALCULATION BOX
calc_box = tk.Text(root, height=12, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
calc_box.bind("<FocusIn>", lambda event: calc_box.delete(1.0, tk.END))
calc_box.grid(row=6, column=0, padx=20, pady=10, sticky="nsew", columnspan=2)

# BOTTOM SPACER BOX
bot_space = tk.Entry(root, width=100, bg="#CACBD1", fg="#CACBD1", bd=0)
bot_space = bot_space.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

# GRAPH BOX
graph_box = tk.Entry(root, width=100, bg="white", fg="white", bd=0)
graph_box.grid(row=3, rowspan=4, column=3, columnspan=2, padx=20, pady=10, sticky="nse")


#________________________________________________________FUNCTIONS________________________________________________________#

# Function to handle file selection from directory browser
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        dir_box.delete(0, tk.END)
        dir_box.insert(0, file_path)
        with open(file_path, "r") as file:
            file_contents = file.read()
            file_box.delete(1.0, tk.END)
            file_box.insert(tk.END, file_contents)

# Define the function to generate the graph
def generate_graph():
    # Generate some data to plot
    x = np.linspace(-5, 5, 100)
    y = x ** 2
    
    # Create a new figure and plot the data
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    
    # Create a Tkinter canvas to display the figure
    canvas = FigureCanvasTkAgg(fig, master=graph_box)
    canvas.draw()
    
    # Update the graph_box with the canvas
    graph_box.delete(0, tk.END)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    graph_box.insert(0, "Graph generated successfully!")
            
# Function to clear text from all textboxes
def clear_text():
    dir_box.delete(0, tk.END)
    dir_box.insert(0, " Enter file path")
    file_box.delete(1.0, tk.END)
    file_box.insert(tk.END, ' File contents will be displayed here.\n\n If entering manually, use the following format (include quotations):\n\n "Last","First","Student ID","Grade"')
    calc_box.delete(1.0, tk.END)
    calc_box.insert(tk.END, "")
    
# Function to exit program
def exit_program():
    root.destroy()

#__________________________________________________________BUTTONS________________________________________________________#

# BROWSE BUTTON
browse_button = ttk.Button(root, text="Browse", width=10)
browse_button.grid(row=4, column=0, pady=10, padx=20, sticky="w")

# CALCULATE BUTTON
calc_button = ttk.Button(root, text="Calculate", width=10)
calc_button.grid(row=4, column=0, pady=10, padx=20, sticky="n")

# CLEAR BUTTON
clear_button = ttk.Button(root, text="Clear", width=10)
clear_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")

# EXIT BUTTON
exit_button = ttk.Button(root, text="Exit", command=exit_program, width=10)
exit_button.grid(row=1, column=4, sticky="ne", padx=7, pady=7)

#___________________________________________________________ATTACH________________________________________________________#
    
# Attach select_file function to browse button
browse_button.config(command=select_file)

# Attach clear_text function to clear button
clear_button.config(command=clear_text)
# Attach calculate function to calculate button

def test():
    data = main.fetch(dir_box.get())
    sec_data = data[0]
    grp_data = data[1]

    sec_data.keys()

    generate_graph()

    data2 = sec_data[list(sec_data.keys())[1]]

    datastr = str(data2)

    datastr += "\n" + "Mean of section: " + str(data2["mean"])
    datastr += "\n" + str(data2["stddev"])
    #str += "\n" + data2["stdev"] 
    calc_box.insert(tk.END, datastr)

    #calc_box.insert(tk.END, data[0]["COMSC110S20.SEC"])

calc_button.config(command=lambda: [test()])

#__________________________________________________________WEIGHTS________________________________________________________#

# Set grid weights to allow for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(3, weight=1)

root.mainloop()

