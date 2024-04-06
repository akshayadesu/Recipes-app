# Forgotpassword.py

import tkinter as tk
from tkinter import messagebox
import sqlite3

def reset_password():
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Check if the username exists
    username = username_entry.get()
    cursor.execute('''SELECT * FROM users WHERE username=?''', (username,))
    user = cursor.fetchone()

    if user:
        # Update the password
        new_password = new_password_entry.get()
        cursor.execute('''UPDATE users SET password=? WHERE username=?''', (new_password, username))
        conn.commit()
        conn.close()
        messagebox.showinfo("Password Reset", "Your password has been reset successfully.")
        root_forgot_password.destroy()
    else:
        messagebox.showerror("Error", "Username not found.")

# Create the root window for password reset
root_forgot_password = tk.Tk()
root_forgot_password.title("Forgot Password")
root_forgot_password.geometry("400x300")
root_forgot_password.config(bg="#ADD8E6")

# Custom font
custom_font = ("Helvetica", 16)

# Create a frame to hold the password reset form
frame = tk.Frame(root_forgot_password, bg='lightblue')
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Username
username_label = tk.Label(frame, text='Username:', font=custom_font, bg='lightblue')
username_label.pack(pady=7)

username_entry = tk.Entry(frame, width=20, font=custom_font, borderwidth=3)
username_entry.pack(pady=2)

# New Password
new_password_label = tk.Label(frame, text='New Password:', font=custom_font, bg='lightblue')
new_password_label.pack(pady=7)

new_password_entry = tk.Entry(frame, width=20, font=custom_font, borderwidth=3, show='*')
new_password_entry.pack(pady=2)

# Reset Password button
reset_button = tk.Button(frame, text='Reset Password', command=reset_password, width=15, font=custom_font, bg='green', fg='white')
reset_button.pack(pady=20)

root_forgot_password.mainloop()
