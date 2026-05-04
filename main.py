# Calorie Calculator 

# START PROGRAM 
import tkinter as tk
from tkinter import ttk

# Create GUI window
root = tk.Tk()
# Set window title and size
root.title("Calorie Calculator")
root.geometry("320x465")

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

# CREATE RADIOBUTTONS (Goal)

goal_var = tk.StringVar()
goal_var.set("Maintain")

tk.Radiobutton(root, text="Lose weight", variable=goal_var, value="Lose").pack()
tk.Radiobutton(root, text="Maintain weight", variable=goal_var, value="Maintain").pack()
tk.Radiobutton(root, text="Gain weight", variable=goal_var, value="Gain").pack()
# CREATE CALCULATE BUTTON

# Shows results
result_label = tk.Label(root, text="")
result_label.pack()

# WHEN BUTTON CLICKED
def calculate():
    try:
        # - Get weight input
        weight = float(weight_entry.get())

        # - Calculate base calories = weight × 22
        calories = weight * 22

        # IF goal = lose weight
        # subtract 300 calories
        if goal_var.get() == "Lose":
            calories -= 300

        # IF goal = gain weight
        # add 300 calories
        elif goal_var.get() == "Gain":
            calories += 300

# APPLY ACTIVITY MULTIPLIER:
# - Inactive → ×1.2
# - Light → ×1.4
# - Moderate → ×1.6
# - Active → ×1.8

# DISPLAY RESULT ON SCREEN

# RUN PROGRAM
root.mainloop()