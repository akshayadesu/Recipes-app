import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

def login_action():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Query the database for the user's credentials
    cursor.execute('''SELECT * FROM users WHERE username=? AND password=?''', (username, password))
    user = cursor.fetchone()

    # Close the connection
    conn.close()

    # Check if user exists and credentials are correct
    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        import home
    else:
        messagebox.showerror("Error", "Invalid username or password")

def open_forgot_password_page():
    os.system('python Forgotpassword.py')

# Create main window
root = tk.Tk()
root.title("Login")
root.geometry("400x300")
root.config(bg="#ADD8E6")

# Custom font
custom_font = ("Helvetica", 16)

# Create a frame to hold the login form
frame3 = tk.Frame(root, bg='lightblue')
frame3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Username
username_label = tk.Label(frame3, text='Username:', font=custom_font, bg='lightblue')
username_label.pack(pady=7)

username_entry = tk.Entry(frame3, width=20, font=custom_font, borderwidth=3)
username_entry.pack(pady=2)

# Password
password_label = tk.Label(frame3, text='Password:', font=custom_font, bg='lightblue')
password_label.pack(pady=7)

password_entry = tk.Entry(frame3, width=20, font=custom_font, borderwidth=3, show='*')
password_entry.pack(pady=2)

# Login button
login_button = tk.Button(frame3, text='Login', command=login_action, width=10, font=custom_font, bg='green', fg='white')
login_button.pack(pady=20)

# Forget Password button
forget_password_button = tk.Button(root, text='Forget Password', command=open_forgot_password_page, font=custom_font, bg='yellow')
forget_password_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
