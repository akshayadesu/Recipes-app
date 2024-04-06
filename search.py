import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import webbrowser


# Function to fetch recipe information from the database
def fetch_recipe_information(search_query):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('recipes.db')
        cursor = conn.cursor()

        # Execute the query to retrieve recipe information
        cursor.execute('''SELECT name, ingredients, procedure, youtube_link, image_path FROM recipes WHERE name=?''', (search_query,))
        recipe_info = cursor.fetchone()

        # Close the connection
        conn.close()

        if recipe_info:
            return recipe_info  # Return all recipe details
        else:
            return None  # Recipe not found.

    except sqlite3.Error as e:
        print("Error fetching recipe information:", e)
        return None

# Function to search for a recipe and display its information
def search_recipe():
    search_query = search_entry.get()
    recipe_info = fetch_recipe_information(search_query)
    if recipe_info:
        name_label.config(text=recipe_info[0])  # Display recipe name
        ingredients_text.delete("1.0", tk.END)
        ingredients_text.insert(tk.END, recipe_info[1])  # Display recipe ingredients
        procedure_text.delete("1.0", tk.END)
        procedure_text.insert(tk.END, recipe_info[2])  # Display recipe procedure
        youtube_link_label.config(text="Youtube Link: " + recipe_info[3], cursor="hand2", fg="blue")
        youtube_link_label.bind("<Button-1>", lambda e: webbrowser.open(recipe_info[3]))  # Open YouTube link when clicked
        image_path = recipe_info[4]  # Get image path from database
        if image_path:
            try:
                image = Image.open(image_path)
                image = image.resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)  # Display recipe image
                image_label.image = photo
            except FileNotFoundError:
                print("Image file not found:", image_path)
        else:
            # If no image is available, display a placeholder or leave it blank
            pass
    else:
        name_label.config(text="Recipe not found.")
        ingredients_text.delete("1.0", tk.END)
        procedure_text.delete("1.0", tk.END)
        youtube_link_label.config(text="", cursor="", fg="black")
        image_label.config(image=None)

# Function to open the home page
def open_home_page():
    home_window = tk.Tk()
    home_window.title("Search - Gujarathi and Rajasthani Recipes")
    home_window.geometry("600x500")
    home_window.configure(bg="lavender")

    label = tk.Label(home_window, text="Explore the Vibrant World of Gujarathi and Rajasthani Recipes!", font=("Arial", 20, "bold"), bg="lavender", fg="#333333")
    label.pack(pady=10)

    search_frame = tk.Frame(home_window, bg="lavender")
    search_frame.pack(pady=20)

    search_label = tk.Label(search_frame, text="Search for Recipes:", font=("Arial", 14), bg="lavender", fg="#333333")
    search_label.grid(row=0, column=0, padx=10, pady=10)

    global search_entry
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    button_search = tk.Button(search_frame, text="Search", width=10, bg="#009688", fg="white", font=("Arial", 12, "bold"), command=search_recipe)
    button_search.grid(row=0, column=2, padx=10, pady=10)

    global name_label
    name_label = tk.Label(home_window, text="", font=("Arial", 16), bg="lavender", fg="#333333")
    name_label.pack(pady=10)

    global ingredients_text
    ingredients_text = tk.Text(home_window, height=5, width=50, font=("Arial", 12), bg="#E0E0E0", fg="#333333")
    ingredients_text.pack(pady=10)

    global procedure_text
    procedure_text = tk.Text(home_window, height=10, width=50, font=("Arial", 12), bg="#E0E0E0", fg="#333333")
    procedure_text.pack(pady=10)

    global youtube_link_label
    youtube_link_label = tk.Label(home_window, text="", font=("Arial", 12), bg="lavender", fg="blue")
    youtube_link_label.pack(pady=10)

    global image_label
    image_label = tk.Label(home_window, bg="white")
    image_label.pack()

    home_window.mainloop()

open_home_page()
