import tkinter as tk
from tkinter import filedialog
import os
import re
import sys

def select_file():
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename()
    if not file_path:
        sys.exit() 
    return file_path

def read_file():
    while True:
        file_path = select_file()
        if os.path.exists(file_path):
            return file_path
        else:
            print("File not found or no file selected. Please select a valid file.")
            continue

def verification(content):

    patterns = {
        'name': re.compile(r"Name: [A-Za-zÁáÉéÍíÓóÖöŐőÚúÜüŰű]{2,25}\s[A-Za-zÁáÉéÍíÓóÖöŐőÚúÜüŰű-]{2,25}"),
        'phone': re.compile(r"Phone: \d{10}"),
        'address': re.compile(r"Address: \d{1,3}, [A-Za-zÁáÉéÍíÓóÖöŐőÚúÜüŰű]{2,20} Street"),
        'bill': re.compile(r"Product: (.+), Price: (\d+\.\d{2}), TVA: (\d+\.\d{2})%, Quantity: (\d+)"),
    }

    errors = []

    for pattern_name, pattern in patterns.items():
        match = pattern.search(content)
        if not match:
            errors.append(f"Error at {pattern_name.replace('_', ' ')}.")

    return errors

file_path = read_file()
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

data_sets = content.strip().split("\n\n")

for i, data_set in enumerate(data_sets, start=1):
    print(f"Processing Data Set {i}:")
    errors = verification(data_set)

    if not errors:
        print("The data set respects the formatting requirements.")
    else:
        print("The data set does not respect the formatting requirements. Errors:")
        for error in errors:
            print(error)
    print()
