import tkinter as tk
from PIL import ImageTk, Image

def open_search_page():
    import search

def open_share_page():
    import enter

def open_home_page():
    # Create a new window for the home page
    home_window = tk.Tk()
    home_window.title("Home - Gujarathi and Rajasthani Recipes")

    # Set background color
    home_window.configure(bg="lavender")

    # Add content to the home page
    label = tk.Label(home_window, text="Explore the Vibrant World of Gujarathi and Rajasthani Recipes!", font=("Times New Roman",30, "bold"), bg="lavender")
    label.pack(pady=10)

    text = """
    Opt your choice
    """
    text_label = tk.Label(home_window, text=text, font=("Arial", 20), bg="lavender")
    text_label.pack(pady=30)

    button1 = tk.Button(home_window, text="Share For Recipes", 
                   width=20, height=5, bg="violet", fg="black", font=("Arial", 30),command=open_share_page)
    
    
    button1.pack(side='right',pady=10,padx=50)

    button2 = tk.Button(home_window, text="Search Your Recipes", 
                   width=20, height=5, bg="light green", fg="black", font=("Arial", 30),command=open_search_page)
    
    button2.pack(pady=20,padx=50)

    # Run the Tkinter event loop for the home page window
    home_window.mainloop()

# Call the function to open the home page immediately upon running the script
open_home_page()