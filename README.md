# 🔐 Password Strength Checker

## Overview
Password Strength Checker is a user-friendly GUI tool to evaluate the strength of passwords. It provides instant feedback on password security and suggests improvements, ensuring users create strong and secure passwords.

## Features
- **Real-Time Feedback**: Instantly assess the strength of your password as you type.
- **Strength Levels**: Categorize password strength into **Strong**, **Moderate**, or **Weak**.
- **Color-Coded Boxes**: Visual representation of password strength using color codes:
  - Green: Strong
  - Yellow: Moderate
  - Red: Weak
  - Grey: Empty slots
- **Suggestions**: Provides actionable recommendations for improving weak passwords.
- **Password Visibility Toggle**: View or hide your password with a simple button.

## Prerequisites
Before running the application, ensure you have:
- Python 3.6 or higher installed on your system.
- The `tkinter` library (pre-installed with Python).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/Password-Strength-Evaluator.git
## Navigate to The Project Directory
   
    cd Password-Strength-Evaluator.py

## How To Run
1.Open  a terminal or command promt.
2.Run the script.
    
    python3 Password-Strength-Evaluator.py     
3.The GUI will open ,and you start testing your passwords. 
    
## Code Overview
  This project includes the following key components:
   - check_password_strength function: Evaluates password against criteria (length, uppercase, lowercase, digit, special character) and returns strength, score, and suggestions.
   - update_strength function: Updates GUI elements such as password strength label, color-coded boxes, and suggestions in real time.
   - toggle_password function: Enables users to toggle password visibility.
   - GUI setup: Constructs the graphical interface using the tkinter module.

## Usage
- Enter your password in the provided field.
- View the strength label to know how secure your password is.
- Check the color-coded boxes for a visual representation of your password strength.
- Follow the suggestions to improve your password (if necessary).
- Use the Show/Hide button to toggle password visibility.

## Contributing
Want to enhance this tool? Fork the project and submit your pull requests. Contributions are welcome!

## THANK YOU !

