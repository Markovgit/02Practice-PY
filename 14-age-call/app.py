import tkinter as tk
from datetime import datetime

def calculate_age():
    birth_date_str = birth_date_entry.get()
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_label.config(text=f"You are {age} years old.")
    except ValueError:
        age_label.config(text="Please enter a valid date in YYYY-MM-DD format.")

# Creating the main window
root = tk.Tk()
root.title("Age Calculator")

# Label and Entry for birth date
birth_date_label = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):")
birth_date_label.pack()
birth_date_entry = tk.Entry(root)
birth_date_entry.pack()

# Button to calculate age
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

# Label to display the age
age_label = tk.Label(root, text="")
age_label.pack()

# Run the Tkinter event loop
root.mainloop()
