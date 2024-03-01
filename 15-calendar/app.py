import tkinter as tk
import calendar

def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal = calendar.month(year, month)
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Calendar for {}/{}:\n".format(month, year))
    result_text.insert(tk.END, cal)
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Calendar")

# Year input
year_label = tk.Label(root, text="Enter year:")
year_label.grid(row=0, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)

# Month input
month_label = tk.Label(root, text="Enter month (1-12):")
month_label.grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

# Button to show calendar
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=2, columnspan=2)

# Display area for the calendar
result_text = tk.Text(root, height=10, width=25)
result_text.grid(row=3, columnspan=2)
result_text.config(state=tk.DISABLED)

root.mainloop()
