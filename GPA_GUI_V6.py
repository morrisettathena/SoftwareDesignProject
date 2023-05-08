#__________________________________________________________TITLES_________________________________________________________#

import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import main
import pandas
import util
from tkinter import * 
from tkinter.ttk import *
import matplotlib.ticker as ticker
from pandastable import Table, TableModel
from tkinter import scrolledtext

root = tk.Tk()
root.title("GPA Calculator")
root.config(bg='#CACBD1')
#root.attributes('-fullscreen', True)
root.geometry('1280x800')
root.resizable(width=0, height=0)

#data to be stored for every .RUN file
index: int = 0
sec_data = None
grp_data = None
pages: list = None

# ROGER WILLIAMS LABEL
title_label = ttk.Label(root, text="   Roger Williams", font=("Times New Roman", 20), foreground="white", background="#003865")
title_label.grid(row=1, column=0, columnspan=5, pady=(10, 0), sticky="nsew")

# UNIVERSITY LABEL
univ_label = ttk.Label(root, text="  University", font=("Times New Roman", 27), foreground="#A4C8E1", background="#003865")
univ_label.grid(row=2, column=0, columnspan=5, pady=(0, 45), sticky="nsew")


#__________________________________________________________TEXTBOXES______________________________________________________#

# TOP SPACER BOX
top_space = tk.Entry(root, width=500, bg="#003865", fg="#003865", bd=0)
top_space = top_space.grid(row=0, rowspan=2, columnspan=5, pady=(0,30) , column=0, sticky="nesw")

# FILE DIRECTORY BOX
dir_box = tk.Entry(root, width=80, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
dir_box.insert(0, " Enter file path")
dir_box.bind("<FocusIn>", lambda event: dir_box.delete(0, tk.END))
dir_box.grid(row=3, column=0, padx=20, pady=10, sticky="w")

# FILE CONTENTS BOX
file_box = tk.Text(root, height=3, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
file_box.insert(INSERT, ' File contents will be displayed here.')
file_box.grid(row=5, column=0, padx=20, pady=10, sticky="w", columnspan=2)

# STUDENT BOX
student_box = Text(root, height=7, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
student_box.insert(INSERT, ' Results in this box will only show up for .SEC files')
student_box.grid(row=6, column=0, padx=20, pady=10, sticky="w", columnspan=2)
student_box.grid_propagate(False)

# CALCULATION BOX
calc_box = tk.Text(root, height=12, font=("Arial", 14), bg="white", fg="#a3a3a3", bd=0)
calc_box.grid(row=7, column=0, padx=20, pady=10, sticky="nsew", columnspan=2)

# BOTTOM SPACER BOX
bot_space = tk.Entry(root, width=100, bg="#CACBD1", fg="#CACBD1", bd=0)
bot_space = bot_space.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

# GRAPH BOX
graph_box = tk.Entry(root, width=100, bg="white", fg="white", bd=0)
graph_box.grid(row=3, rowspan=5, column=3, columnspan=2, padx=20, pady=10, sticky="nse")


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

def generate_graph(dictData: dict):
    global index, pages, grp_data, sec_data

    for item in graph_box.winfo_children():
        item.destroy()

    fig = plt.Figure(figsize=(6, 4))
    a = fig.add_subplot(111)

    ls = sorted([(k, v) for k, v in dictData.items()], key = lambda x:x[0])
    ls2 = list(zip(*ls))


    a.bar(ls2[0], ls2[1])
    a.set_xlabel("Grades")
    a.set_ylabel("Number of Students")
    a.set_title("Distribution of Grades")
    # Add bar chart to window
    canvas = FigureCanvasTkAgg(fig, master=graph_box)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Return grades and num_students

def clear_text():
    dir_box.delete(0, tk.END)
    dir_box.insert(0, " Enter file path")
    file_box.delete(1.0, tk.END)
    file_box.insert(tk.END, ' File contents will be displayed here.')
    calc_box.delete(1.0, tk.END)
    calc_box.insert(tk.END, "")
    student_box.delete(1.0, tk.END)
    student_box.insert(tk.END, ' Results in this box will only show up for .SEC files')
    for item in graph_box.winfo_children():
            item.destroy()
    for item in student_box.winfo_children():
            item.destroy()


def clear_canvas():
    global graph_canvas, graph_fig, graph_ax
    # Clear the old graph if it exists
    if graph_fig is not None:
        graph_ax.clear()
        graph_fig = None
        #graph_canvas.draw()
        graph_canvas.get_tk_widget().destroy()

# Function to exit program
def exit_program():
    root.destroy()

#__________________________________________________________BUTTONS________________________________________________________#

# LEFT BUTTON
left_button = tk.Button(root, width = 10, text="<<", bd=0, fg='white', bg='#003865')
left_button.grid(row = 3, columnspan=2, column = 3, pady=10, padx=250, sticky='w')

# BROWSE BUTTON
browse_button = ttk.Button(root, text="Browse", width=10)
browse_button.grid(row=4, column=0, pady=10, padx=20, sticky="w")

# CALCULATE BUTTON
calc_button = ttk.Button(root, text="Calculate", width=10)
calc_button.grid(row=4, column=0, pady=10, padx=20, sticky="n")

# CLEAR BUTTON
clear_button = ttk.Button(root, text="Clear", width=10)
clear_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")

# RIGHT BUTTON
right_button = tk.Button(root, text=">>", width = 10, bd=0, fg='white', bg='#003865')
right_button.grid(row = 3, columnspan=2, column = 4, pady=10, padx=210, sticky='e')

# EXIT BUTTON
exit_button = ttk.Button(root, text="Exit", command=exit_program, width=10)
exit_button.grid(row=1, column=4, sticky="ne", padx=7, pady=7)

#___________________________________________________________FUNCTIONS________________________________________________________#

def displayData():
    global index, pages, grp_data, sec_data

    if pages is None:
        return

    # Generate the graph and get the grades and num_students values
    gradeCountsDict = None
    datastr = ""
    if pages[index].endswith("GRP"):
        data2 = grp_data[pages[index]]

        grade_counts = data2["gradecounts"]

        datastr += "\n" + "Group:\t" + str(pages[index])
        datastr += "\n" + "Sections and Z-test:"

        ztestdata = sorted(data2["ztests"].items(), key=lambda x:x[1])
        for item in ztestdata:
            datastr += "\n\t" + str(item[0]) + ":\t " + str(item[1])
            if item[1] >= 2.0:
                datastr += "SIGNIFICANTLY HIGH"
            elif item[1] <= -2.0:
                datastr += "SIGNIFICANTLY LOW"
        datastr += "\n"

        datastr += "\n" + "Mean:\t" + str(data2["mean"])
        datastr += "\n" + "Standard Deviation:\t" + str(data2["stddev"])
        datastr += "\n" + "Number of Students:\t" + str(data2["numstudents"])
        datastr += "\n" + "Grade Counts:"

        gradeCounts = sorted(list(data2["gradecounts"].keys()), key =lambda x:util.getOrder(x), reverse=True)
        for item in gradeCounts:
            datastr += "\n\t" + str(item) + ":\t" + str(data2["gradecounts"][item])

        for grade, count in data2["gradecounts"].items():
            grade_counts[grade] = count
            datastr += "\n\t" + str(grade) + ":\t" + str(count)
        gradeCountsDict = data2["gradecounts"]

        for item in student_box.winfo_children():
            item.destroy()

    elif pages[index].endswith("SEC"):
        data2 = sec_data[pages[index]]

        grade_counts = data2["gradecounts"]

        datastr += "\n" + "Section:\t" + str(pages[index])
        datastr += "\n" + "Credit Hours:\t" + str(data2["creditHours"]) + "\n"
        datastr += "\n" + "Mean:\t" + str(data2["mean"])
        datastr += "\n" + "Standard Deviation:\t" + str(data2["stddev"])
        datastr += "\n" + "Number of Students:\t" + str(data2["numstudents"])
        datastr += "\n" + "Grade Counts:"
        gradeCounts = sorted(list(data2["gradecounts"].keys()), key =lambda x:util.getOrder(x), reverse=True)
        for item in gradeCounts:
            datastr += "\n\t" + str(item) + ":\t" + str(data2["gradecounts"][item])

        gradeCountsDict = data2["gradecounts"]

        students: pandas.DataFrame = data2["data"]

        table = pt = Table(student_box, dataframe = students)
        pt.show()
        gradeCountsDict = data2["gradecounts"]

    generate_graph(gradeCountsDict)
    calc_box.delete("1.0", tk.END)
    calc_box.insert(tk.END, datastr)
    

def shiftIndexRight():
    global index, pages

    if pages == None:
        return 
    
    if len(pages)-1 == index:
        index = 0
    else:
        index += 1

    # Clear graph from canvas
    for widget in graph_box.winfo_children():
        widget.destroy()

    displayData()
    
def shiftIndexLeft():
    global index, pages

    if pages == None:
        return
    
    if index == 0:
        index = len(pages)-1
    else:
        index -= 1
    
    # Clear graph from canvas
    for widget in graph_box.winfo_children():
        widget.destroy()

    displayData()

def sendToOutput(file: str, path: str):
    
    f = open(path + "/" + file + ".STATS", "w")
    for item in grp_data:
        f.write(item + " data: " + str(grp_data[item]) + "\n")
    for item in sec_data:
        z = sec_data[item].copy()
        z.pop("data")
        
        f.write(item + " data: " + str(z) + "\n")
        
    print(path)
    print("sent data to output")
    
def getData():
    global sec_data, grp_data, pages, index

    path = dir_box.get()

    if not path.endswith(".RUN"):
        calc_box.delete("1.0", tk.END)
        calc_box.insert(tk.END, "Not a valid RUN file")
    else:
        data = None
        try:
            data = main.fetch(dir_box.get())
        except Exception:
            calc_box.delete("1.0", tk.END)
            calc_box.insert(tk.END, "Error reading RUN file")
            return
        sec_data = data[0]
        grp_data = data[1]

        runFile = path[path.rindex("/")+1:]
        outputpath = path[:path.rindex("/")]
        sendToOutput(runFile, outputpath)
        
        pages = list(grp_data.keys())
        pages.extend(list(sec_data.keys()))
        index = 0
        displayData()
        
#___________________________________________________________ATTACH________________________________________________________#
    
# Attach select_file function to browse button
browse_button.config(command=select_file)

# Attach clear_text function to clear button
clear_button.config(command=clear_text)

# Attach calc_text function to calc button
calc_button.config(command= getData)

# Attach clear_canvas function to arrow buttons
left_button.config(command = (shiftIndexLeft))
right_button.config(command = shiftIndexRight)

#__________________________________________________________WEIGHTS________________________________________________________#

# Set grid weights to allow for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(3, weight=1)

root.mainloop()