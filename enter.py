import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def submit_recipe():
    # Retrieve recipe information from the form
    recipe_name = recipe_name_entry.get()
    ingredients = ingredients_text.get("1.0", tk.END)
    procedure = procedure_text.get("1.0", tk.END)
    youtube_link = youtube_entry.get()

    # Insert recipe information into the database
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO recipes (name, ingredients, procedure, youtube_link, image_path) 
                      VALUES (?, ?, ?, ?, ?)''', (recipe_name, ingredients, procedure, youtube_link, image_path))
    conn.commit()
    conn.close()

    # Display the entered recipe information (for demonstration)
    print("Recipe Name:", recipe_name)
    print("Ingredients:", ingredients)
    print("Procedure:", procedure)
    print("YouTube Link:", youtube_link)
    print("Image Path:", image_path)

    # Show a message box indicating successful insertion
    messagebox.showinfo("Recipe Inserted", "Recipe inserted successfully!\nImage path: " + image_path)

def upload_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    # Display the selected image
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def open_enter_recipe_page():
    enter_recipe_window = tk.Tk()
    enter_recipe_window.title("Enter Recipe")
    enter_recipe_window.geometry("600x600")
    enter_recipe_window.configure(bg="lavender")

    label = tk.Label(enter_recipe_window, text="Enter New Recipe", font=("Arial", 20, "bold"), bg="lavender", fg="#333333")
    label.pack(pady=10)

    recipe_frame = tk.Frame(enter_recipe_window, bg="lavender")
    recipe_frame.pack(pady=20)

    recipe_name_label = tk.Label(recipe_frame, text="Recipe Name:", font=("Arial", 12), bg="lavender", fg="#333333")
    recipe_name_label.grid(row=0, column=0, padx=10, pady=10)

    global recipe_name_entry
    recipe_name_entry = ttk.Entry(recipe_frame, width=30)
    recipe_name_entry.grid(row=0, column=1, padx=10, pady=10)

    ingredients_label = tk.Label(recipe_frame, text="Ingredients:", font=("Arial", 12), bg="lavender", fg="#333333")
    ingredients_label.grid(row=1, column=0, padx=10, pady=10)

    global ingredients_text
    ingredients_text = tk.Text(recipe_frame, height=5, width=40, font=("Arial", 12), bg="#E0E0E0", fg="#333333")
    ingredients_text.grid(row=1, column=1, padx=10, pady=10)

    procedure_label = tk.Label(recipe_frame, text="Procedure:", font=("Arial", 12), bg="lavender", fg="#333333")
    procedure_label.grid(row=2, column=0, padx=10, pady=10)

    global procedure_text
    procedure_text = tk.Text(recipe_frame, height=10, width=40, font=("Arial", 12), bg="#E0E0E0", fg="#333333")
    procedure_text.grid(row=2, column=1, padx=10, pady=10)

    youtube_link_label = tk.Label(recipe_frame, text="YouTube Link:", font=("Arial", 12), bg="lavender", fg="#333333")
    youtube_link_label.grid(row=3, column=0, padx=10, pady=10)

    global youtube_entry
    youtube_entry = ttk.Entry(recipe_frame, width=30)
    youtube_entry.grid(row=3, column=1, padx=10, pady=10)

    image_upload_button = tk.Button(enter_recipe_window, text="Upload Image", width=15, bg="#009688", fg="white", font=("Arial", 12), command=upload_image)
    image_upload_button.pack(pady=10)

    global image_label
    image_label = tk.Label(enter_recipe_window, bg="lavender")
    image_label.pack(pady=10)

    submit_button = tk.Button(enter_recipe_window, text="Submit", width=10, bg="#009688", fg="white", font=("Arial", 12, "bold"), command=submit_recipe)
    submit_button.pack(pady=20)

    enter_recipe_window.mainloop()

open_enter_recipe_page()
