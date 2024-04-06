import tkinter as tk
import subprocess
from PIL import ImageTk, Image
    
def home():
    subprocess.run(["python","C:/Users/akshaya/Desktop/new wise/home.py"])
def login():
    subprocess.run(["python","C:/Users/akshaya/Desktop/new wise/login.py"])
def  signup():
    subprocess.run(["python","C:/Users/akshaya/Desktop/new wise/signup.py"])
def about():
    subprocess.run(["python","C:/Users/akshaya/Desktop/new wise/about.py"])

root = tk.Tk()
root.title("Rajasthani & Gujrathi recipies!!")

image_path = "bg1.png"
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)

label = tk.Label(root, image=tk_image)
label.pack()


home_button = tk.Button(root, bg="white", fg="blue", text="Home", font=("Arial",17),command=home,borderwidth=3, highlightbackground="black")
home_button.place(x=10, y=20,width=100, height=42)
about_button = tk.Button(root, bg="white", fg="black",text="About", font=("Arial",17),command=about,borderwidth=3, highlightbackground="black")
about_button.place(x=120, y=20, width=100, height=42)

# Create login and signup buttons on the right side
login_button = tk.Button(root, bg="white", fg="black",text="Login",font=("Arial",17), command=login,borderwidth=3, highlightbackground="black")
login_button.place(relx=0.9, y=20, width=100, height=42, anchor="ne")
signup_button = tk.Button(root,bg="white", fg="black", text="Signup",font=("Arial",17), command=signup,borderwidth=3, highlightbackground="black")
signup_button.place(relx=0.8, y=20, width=100, height=42, anchor="ne")

# Run the Tkinter event loop
root.mainloop()