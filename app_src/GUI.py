import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import json

def on_dropdown_change(event):
    """Callback function to show/hide additional fields based on dropdown selection."""
    if dropdown_var.get() == "External Server":
        url_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        url_entry.grid(row=4, column=1, padx=10, pady=5)
        api_key_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        api_key_entry.grid(row=5, column=1, padx=10, pady=5)
    else:
        url_label.grid_remove()
        url_entry.grid_remove()
        api_key_label.grid_remove()
        api_key_entry.grid_remove()

def get_all_values():
    """Retrieve all input values from the GUI."""
    # Collect base values
    width = width_entry.get()
    height = height_entry.get()
    mode = dropdown_var.get()

    # Prepare the result dictionary
    values = {
        "width": width,
        "height": height,
        "mode": mode
    }

    # Include URL and API Key if the mode is 'External Server'
    if mode == "External Server":
        values["url"] = url_entry.get()
        values["api_key"] = api_key_entry.get()

    return values

def on_submit_and_run():
    """Retrieve values, pass them to another program, confirm, and close."""
    values = get_all_values()

    # Save values to a JSON file
    with open("values.json", "w") as f:
        json.dump(values, f)

    # Call another script, passing the JSON file as an argument
    try:
        subprocess.run(["python", "app_src\main.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the program:\n{e}")
        return

    # Confirmation popup
    # confirmation_message = f"Values submitted and program executed successfully.\n\n{values}"
    # messagebox.showinfo("Submission Confirmed", confirmation_message)

    # Close the GUI
    root.destroy()

# Initialize the main application window
root = tk.Tk()
root.title("AI-Sight")

# Width and Height Inputs
width_label = tk.Label(root, text="Width:",font=("Arial", 25))
width_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

width_entry = tk.Entry(root)
width_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height:",font=("Arial", 25))
height_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Dropdown Menu
dropdown_label = tk.Label(root, text="Mode:",font=("Arial", 25))
dropdown_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=dropdown_var, state="readonly", font=("Arial", 12))
dropdown["values"] = ["Run Locally", "External Server"]
dropdown.grid(row=2, column=1, padx=10, pady=5)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# URL and API Key Inputs (initially hidden)
url_label = tk.Label(root, text="URL:",font=("Arial", 25))
url_entry = tk.Entry(root)

api_key_label = tk.Label(root, text="API Key:",font=("Arial", 25))
api_key_entry = tk.Entry(root)

# Submit Button
submit_button = tk.Button(root, text="Submit and Run", command=on_submit_and_run)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
