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
# - Weight input box
# - Height input box

# CREATE DROPDOWN (Activity level)'

# - Inactive
# - Light
# - Moderate
# - Active

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