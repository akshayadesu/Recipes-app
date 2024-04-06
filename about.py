import tkinter as tk

def open_about_page():
    # Create a new window for the about page
    about_window = tk.Tk()
    about_window.title("About World of Recipes")
    about_window.geometry("600x400")
    about_window.configure(bg="#F0F0F0")

    # Add content to the about page
    title_label = tk.Label(about_window, text="World of Recipes", font=("Arial", 24, "bold"), bg="#F0F0F0")
    title_label.pack(pady=10)

    about_text = (
        "World Of Recipes is an application where users can search and share recipes. This is a handy application where every user can search for a variety of recipes and share their favorite recipes with others.\n\n"
        "It could become a personal cookbook for the users. It makes finding recipes easy. With just a click of a button, users can get access to multiple recipes within a second. As recipes are being added regularly, there will always be something new for the users to discover.\n\n"
        "Each recipe provides users with all the information, from the ingredients required to each step required to cook the different dishes. Users need to register and log in to our application. Once logged in, the user is provided with two choices to select: “Search for a recipe” and “Share a recipe”. Users can choose either of them.\n\n"
        "This app has a special feature of sharing the recipes with others which are not well known to everyone. Our app provides the procedure of recipes in a simple way. It could be helpful for people who have less time to cook. So having these features makes it unique and different from other apps."
    )
    about_label = tk.Label(about_window, text=about_text, font=("Arial", 12), bg="#F0F0F0", justify=tk.LEFT)
    about_label.pack(pady=10, padx=20)

    about_window.mainloop()

# Call the function to open the about page immediately upon running the script
open_about_page()
