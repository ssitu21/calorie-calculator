# Calorie Calculator 

# START PROGRAM
import tkinter as tk
from tkinter import ttk

# Create GUI window
root = tk.Tk()
# Set window title and size
root.title("Calorie Calculator")
root.geometry("420x600")

# CREATE INPUT FIELDS

# - Age input box
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()
# - Weight input box
tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()
# - Height input box
tk.Label(root, text="Height (cm)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

# CREATE DROPDOWN (Activity level)'

activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(root, textvariable=activity_var)
activity_dropdown['values'] = ("Inactive", "Light", "Moderate", "Active")
activity_dropdown.current(0)
activity_dropdown.pack()

# CREATE RADIO BUTTONS (Goal)

# - Lose weight
# - Maintain weight
# - Gain weight

# CREATE CALCULATE BUTTON

# WHEN BUTTON CLICKED

# - Get weight input
# - Calculate base calories = weight × 22

# IF goal = lose weight

# subtract 300 calories

# IF goal = gain weight

# add 300 calories

# APPLY ACTIVITY MULTIPLIER:
# - Inactive → ×1.2
# - Light → ×1.4
# - Moderate → ×1.6
# - Active → ×1.8

# DISPLAY RESULT ON SCREEN

# RUN PROGRAM
root.mainloop()