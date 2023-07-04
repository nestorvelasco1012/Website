#!/usr/bin/env pythonw

import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the function to select the CSV file
def select_csv_file():
    desktop_path = os.path.expanduser("~/Desktop")
    csv_path = filedialog.askopenfilename(initialdir=desktop_path, filetypes=[("CSV files", "*.csv")])
    csv_entry.delete(0, tk.END)
    csv_entry.insert(0, csv_path)


# Define the function to select the folder
def select_folder():
    initial_dir = os.path.expanduser("~/Desktop/Vel-Am Corp/PDF Pending")
    folder_path = filedialog.askdirectory(initialdir=initial_dir)
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

# Define the function to delete files based on the CSV list
def delete_files():
    csv_path = csv_entry.get()
    folder_path = folder_entry.get()
    if csv_path and folder_path:
        with open(csv_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            file_list = [row[0] for row in csv_reader]
        num_deleted = 0
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name in file_list:
                os.remove(file_path)
                num_deleted += 1
        message = f"{num_deleted} files deleted!"
        messagebox.showinfo(title="Done", message=message)
    else:
        messagebox.showerror(title="Error", message="Please select a CSV file and a folder.")

# Create the main window
root = tk.Tk()
root.title("Delete Files")

# Center the window on the screen
window_width = 700
window_height = 130
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Create the label and entry for the CSV file path
csv_label = tk.Label(root, text="CSV file:")
csv_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
csv_entry = tk.Entry(root, width=50)
csv_entry.grid(row=0, column=1, padx=5, pady=5)
csv_button = tk.Button(root, text="Select CSV", command=select_csv_file)
csv_button.grid(row=0, column=2, padx=5, pady=5)

# Create the label and entry for the folder path
folder_label = tk.Label(root, text="Folder:")
folder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=1, column=1, padx=5, pady=5)
folder_button = tk.Button(root, text="Select Folder", command=select_folder)
folder_button.grid(row=1, column=2, padx=5, pady=5)

# Create the button to delete files
delete_button = tk.Button(root, text="Delete Files", command=delete_files)
delete_button.grid(row=2, column=1, padx=5, pady=5)

# Run the main loop
root.mainloop()
