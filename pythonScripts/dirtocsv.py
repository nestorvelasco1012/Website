#!/usr/bin/env pythonw

import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the function to select the folder
def select_folder():
    folder_path = filedialog.askdirectory(initialdir="/Users/AlejandroVelaco/Desktop/Vel-Am Corp/PDF Pending")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

# Define the function to create the CSV file
def create_csv():
    folder_path = folder_entry.get()
    if folder_path:
        folder_name = os.path.basename(folder_path)
        csv_filename = folder_name + ".csv"
        with open(os.path.expanduser("~/Desktop/" + csv_filename), 'w') as csvfile:
            writer = csv.writer(csvfile)
            for filename in os.listdir(folder_path):
                if filename.endswith(".pdf"):
                    name = filename[:-4]  # Remove the ".pdf" extension
                    writer.writerow([name])
        messagebox.showinfo(title="Done", message="CSV file created!")
    else:
        messagebox.showerror(title="Error", message="Please select a folder.")

# Create the main window
root = tk.Tk()
root.title("Directory to CSV")

# Center the window on the screen
window_width = 660
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Create the label and entry for the folder path
folder_label = tk.Label(root, text="Folder:")
folder_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
folder_button = tk.Button(root, text="Select Folder", command=select_folder)
folder_button.grid(row=0, column=2, padx=5, pady=5)

# Create the button to create the CSV file
create_button = tk.Button(root, text="Create CSV", command=create_csv)
create_button.grid(row=1, column=1, padx=5, pady=5)

# Run the main loop
root.mainloop()
