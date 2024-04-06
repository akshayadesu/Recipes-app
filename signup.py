import tkinter as tk
from tkinter import messagebox
import sqlite3

def validate_signup():
    username = username_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
    re_enter_password = re_enter_password_entry.get()

    # Simple validation for demonstration purposes
    if not (username and email and age and gender and password and re_enter_password):
        messagebox.showerror("Error", "Please fill in all fields")
    elif password != re_enter_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        try:
            # Connect to the database
            conn = sqlite3.connect('user_database.db')
            cursor = conn.cursor()

            # Insert user data into the database
            cursor.execute('''INSERT INTO users (username, email, age, gender, password) 
                              VALUES (?, ?, ?, ?, ?)''', (username, email, age, gender, password))

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()

            messagebox.showinfo("Sign-up Successful", "Welcome, " + username + "!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error occurred: " + str(e))


def open_login_window():
    # Close the sign-up window
    signup_window.destroy()

    # Open the login window
    import login

# Create sign-up window
signup_window = tk.Tk()
signup_window.title("Sign-up")
signup_window.geometry("400x400")
signup_window.config(bg="#ADD8E6")

# Custom font
custom_font = ("Helvetica", 16)

# Sign-up Frame
signup_frame = tk.Frame(signup_window, bg="#ADD8E6")
signup_frame.place(relx=0.5, rely=0.5, anchor="center")

# Username
username_label = tk.Label(signup_frame, text="Username:", font=custom_font, bg="#ADD8E6")
username_label.grid(row=0, column=0, padx=5)
username_entry = tk.Entry(signup_frame, font=custom_font)
username_entry.grid(row=0, column=1, padx=5)

# Email
email_label = tk.Label(signup_frame, text="Email:", font=custom_font, bg="#ADD8E6")
email_label.grid(row=1, column=0, padx=10)
email_entry = tk.Entry(signup_frame, font=custom_font)
email_entry.grid(row=1, column=1, padx=10)

# Age
age_label = tk.Label(signup_frame, text="Age:", font=custom_font, bg="#ADD8E6")
age_label.grid(row=2, column=0, padx=5)
age_entry = tk.Entry(signup_frame, font=custom_font)
age_entry.grid(row=2, column=1, padx=5)

# Gender
gender_label = tk.Label(signup_frame, text="Gender:", font=custom_font, bg="#ADD8E6")
gender_label.grid(row=3, column=0, padx=5)
gender_var = tk.StringVar()
gender_choices = ["Male", "Female", "Other"]
gender_dropdown = tk.OptionMenu(signup_frame, gender_var, *gender_choices)
gender_dropdown.grid(row=3, column=1, padx=5)

# Password
password_label = tk.Label(signup_frame, text="Password:", font=custom_font, bg="#ADD8E6")
password_label.grid(row=4, column=0, padx=5)
password_entry = tk.Entry(signup_frame, show="*", font=custom_font)
password_entry.grid(row=4, column=1, padx=5)

# Re-enter Password
re_enter_password_label = tk.Label(signup_frame, text="Re-enter Password:", font=custom_font, bg="#ADD8E6")
re_enter_password_label.grid(row=5, column=0, padx=5)
re_enter_password_entry = tk.Entry(signup_frame, show="*", font=custom_font)
re_enter_password_entry.grid(row=5, column=1, padx=5)

# Sign-up button
signup_button = tk.Button(signup_frame, text="Sign Up", command=validate_signup, font=custom_font)
signup_button.grid(row=6, columnspan=2, pady=10)

# "Already have an account?" link
login_link = tk.Label(signup_window, text="Already have an account? Click here to login", font=('Arial', 11), fg='blue', cursor='hand2')
login_link.place(relx=0.5, rely=0.8, anchor="center")

# Function to open login window
def open_login_window_callback(event):
    open_login_window()

login_link.bind("<Button-1>", open_login_window_callback)

signup_window.mainloop()
