#!/usr/bin/env pythonw

import os
import csv
import glob
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
window = tk.Tk()
window.title("Merge CSV Files")
window.geometry("400x200")

# Create a label for the user prompt
prompt_label = tk.Label(window, text="Select the folder containing the CSV files:")
prompt_label.pack(pady=10)

def browse_folder():
    # Set the initial directory to the desktop
    initial_dir = os.path.expanduser("~/Desktop")
    # Open a file dialog to select the folder
    folder_path = filedialog.askdirectory(initialdir=initial_dir)

    # Update the folder entry widget with the selected folder path
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

# Create a button to browse for the folder
browse_button = tk.Button(window, text="Browse", command=browse_folder)
browse_button.pack()

# Create an entry widget for the folder path
folder_entry = tk.Entry(window, width=30)
folder_entry.pack(pady=10)

def merge_csv_files():
    # Get the folder path from the entry widget
    weekly_folder_path = folder_entry.get()

    # Check if the folder exists
    if not os.path.exists(weekly_folder_path):
        error_label.config(text=f"Error: folder '{weekly_folder_path}' not found.")
        return

    # Change the current working directory to the weekly folder
    os.chdir(weekly_folder_path)

    # Specify the file names of the CSV files to be merged
    filenames = glob.glob("*.csv")
    filenames.sort() # sort the filenames alphabetically

    # create an empty list to store the data from each file
    rows = []

    # open each file and read the data into the "rows" list
    for filename in filenames:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if any(row): # check if the row is not empty
                    rows.append(row)

    # specify the name of the output file
    output_filename = "SEI 2023.csv"

    # write the data to the output file
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # Clear the folder entry widget and display success message
    folder_entry.delete(0, tk.END)
    error_label.config(text="Successfully merged CSV files", fg="green")

# Create a button to run the script
run_button = tk.Button(window, text="Merge CSV Files", command=merge_csv_files)
run_button.pack(pady=10)

# Create a label for error messages
error_label = tk.Label(window, fg="red")
error_label.pack()

# Center the window on the screen
window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))

# Start the Tkinter event loop
window.mainloop()
