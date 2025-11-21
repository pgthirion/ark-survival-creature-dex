# Import necessary libraries
import os
import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from datetime import datetime
import webbrowser
from tkinter import PhotoImage

# Function to display creature information in the text box
def print_creatures(creatures, title, excluded_attribute=None):
    text_box.delete(1.0, tk.END)  # Clear the text box
    text_box.insert(tk.END, f"{title.upper()}\n" + "=" * len(title) + "\n")
    for creature in creatures:
        for key, value in creature.items():
            if key.lower() != excluded_attribute:
                text_box.insert(tk.END, f"{key.capitalize()}: {value}\n")
        text_box.insert(tk.END, "=" * 30 + "\n\n")

# Function to handle different option selections
def handle_option(option):
    if option == "Random":
        random_creature = random.choice(creature_list)
        print_creatures([random_creature], "Randomly selected creature")
    elif option in attribute_filters:
        filtered_creatures = [creature for creature in creature_list if creature[option].lower() == "yes"]
        print_creatures(filtered_creatures, f"{option.capitalize()} creatures")
    elif option == "Herbivore":
        herbivore_creatures = [creature for creature in creature_list if creature["diet"] == "Herbivore"]
        print_creatures(herbivore_creatures, "Herbivore Creatures")
    elif option == "Carnivore":
        carnivore_creatures = [creature for creature in creature_list if creature["diet"] == "Carnivore"]
        print_creatures(carnivore_creatures, "Carnivore Creatures")

# Function to save data to a text file
def save_data_to_text_file():
    data = text_box.get(1.0, tk.END)
    try:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{current_time}_{selected_option.capitalize()}.txt"
        file_path = os.path.join("saved_data", file_name)

        with open(file_path, "w") as text_file:
            text_file.write(data)
        messagebox.showinfo("Save Successful", f"Data saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error saving data: {e}")

# Function to handle option selection
def select_option(option):
    global selected_option
    selected_option = option
    handle_option(option)

# Extract creature data from website
url = "https://ark.fandom.com/wiki/Creatures"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
creature_table = soup.find("table", {"class": "wikitable"})
creature_list = []

# Loop through table rows and extract creature data
for row in creature_table.find_all("tr")[1:]:
    columns = row.find_all("td")
    creature_data = {
        "name": columns[0].text.strip(),
        "rideable": columns[5].text.strip(),
        "diet": columns[2].text.strip(),
        "temperment": columns[3].text.strip(),
        "tameable": columns[4].text.strip(),
        "breedable": columns[6].text.strip(),
        "creature_id": columns[8].text.strip(),
    }
    creature_list.append(creature_data)

# List of attribute filters
attribute_filters = ["rideable", "tameable", "breedable"]

# Create the main Tkinter window
root = tk.Tk()
root.title("Creature Data Menu")
root.geometry("400x525")  # Set window size
root.configure(bg="black")

# Prevent window from being resized
root.resizable(False, False)

# Create a frame for the text box
text_box_frame = tk.Frame(root, bg="black")
text_box_frame.pack(pady=10)

# Create the scrolled text box for displaying creature information
text_box = scrolledtext.ScrolledText(text_box_frame, width=60, height=10, bg="black", fg="white",
                                     font=("Verdana", 10), wrap=tk.WORD, insertbackground="white")
text_box.pack()

# Create a frame for buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack()

# Create button options
button_options = ["Random"] + attribute_filters + ["Herbivore", "Carnivore"]
for option in button_options:
    button = tk.Button(button_frame, text=option.capitalize(), width=15, command=lambda opt=option: select_option(opt),
                       wraplength=80, bg="black", fg="white", font=("Verdana", 10, "bold"))
    button.pack(padx=10, pady=5)

# Create the save button
save_button = tk.Button(root, text="Save Data to Text File", command=save_data_to_text_file, bg="black", fg="white",
                        font=("Verdana", 10, "bold"))
save_button.pack(padx=10, pady=10, anchor="sw", side="left")

# Create the exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="black", fg="white", font=("Verdana", 10, "bold"))
exit_button.pack(padx=10, pady=10, anchor="se", side="right")

# Create 'saved_data' directory if it doesn't exist
if not os.path.exists("saved_data"):
    os.makedirs("saved_data")

# Set the initial selected option and handle it
selected_option = "Random"
handle_option(selected_option)

# Start the Tkinter event loop
root.mainloop()
