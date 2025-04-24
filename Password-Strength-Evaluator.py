import re
import tkinter as tk
from tkinter import ttk

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if not length_criteria:
        feedback.append("• At least 8 characters.")
    if not uppercase_criteria:
        feedback.append("• Add an uppercase letter.")
    if not lowercase_criteria:
        feedback.append("• Add a lowercase letter.")
    if not digit_criteria:
        feedback.append("• Include a number.")
    if not special_char_criteria:
        feedback.append("• Add a special character (!@#$...).")

    return strength, score, feedback

def update_strength(event=None):
    password = password_var.get()
    strength, score, suggestions = check_password_strength(password)

    # Update strength label
    strength_label.config(text=strength)

    # Update color boxes
    for i, box in enumerate(color_boxes):
        if i < score:
            if score == 5:
                box.config(bg="#28a745")  # Green
            elif score >= 3:
                box.config(bg="#ffc107")  # Yellow
            else:
                box.config(bg="#dc3545")  # Red
        else:
            box.config(bg="#e0e0e0")  # Grey for empty slots

    # Update suggestions
    suggestion_box.config(state='normal')
    suggestion_box.delete(1.0, tk.END)

    if suggestions:
        for suggestion in suggestions:
            suggestion_box.insert(tk.END, suggestion + "\n")
    else:
        suggestion_box.insert(tk.END, "✅ Great password!")
    suggestion_box.config(state='disabled')

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_button.config(text='Show')
    else:
        password_entry.config(show='')
        show_button.config(text='Hide')

# GUI setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("420x400")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

ttk.Label(root, text="Enter your password:", background="#f8f9fa", font=('Segoe UI', 11)).pack(pady=(20, 5))

password_var = tk.StringVar()
frame = ttk.Frame(root)
frame.pack()

password_entry = ttk.Entry(frame, textvariable=password_var, show='*', width=30, font=('Segoe UI', 11))
password_entry.grid(row=0, column=0, padx=5)
password_entry.bind('<KeyRelease>', update_strength)

show_button = ttk.Button(frame, text="Show", width=6, command=toggle_password)
show_button.grid(row=0, column=1)

# Strength label
strength_label = tk.Label(root, text="", font=('Segoe UI', 12, 'bold'), bg="#f8f9fa")
strength_label.pack(pady=5)

# Color strength boxes
box_frame = tk.Frame(root, bg="#f8f9fa")
box_frame.pack(pady=5)
color_boxes = []
for _ in range(5):
    box = tk.Label(box_frame, width=4, height=2, bg="#e0e0e0", relief='solid', bd=1)
    box.pack(side='left', padx=4)
    color_boxes.append(box)

# Suggestions
ttk.Label(root, text="Suggestions:", background="#f8f9fa", font=('Segoe UI', 10)).pack()
suggestion_box = tk.Text(root, height=6, width=50, wrap="word", state='disabled', font=('Segoe UI', 10))
suggestion_box.pack(pady=5)

root.mainloop()
