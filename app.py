from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

"""
# Project 20: Password Manager

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 27 Dec 2024

## Description:
A Password Manager application with a user-friendly GUI to store, manage, and retrieve passwords securely. It generates random passwords, copies them to the clipboard automatically, and stores user-provided credentials (website, username, password) in a JSON file. The app includes features for error handling, user input validation, search functionality, and a lock icon for visual appeal.

## How to Use:
1. Enter the website name in the provided field.
2. To search for existing credentials:
   - Enter the website name in the website field and click the "Search" button.
   - If the data exists, it will display the email and password for the entered website.
   - If no data is found, it will alert you: "No data found for this website-name."
3. To add new credentials:
   - Provide the website, email/username, and password fields.
   - Generate a strong random password using the "Generate Password" button if needed.
   - Crosscheck the entered information when prompted.
   - Click the "Add" button to save the details in `data.json`.
4. If the password is generated, it will be automatically copied to the clipboard.

## Level
- **Level**: Intermediate, automation project with added functionality.
- **Skills:** Python programming, file handling, GUI development with Tkinter, JSON manipulation, clipboard handling, error handling.
- **Domain:** Task automation, password management, GUI applications.

## Features
- Generates strong random passwords using a mix of characters.
- Automatically copies generated passwords to the clipboard.
- Validates user input to ensure no fields are left empty.
- Prompts the user to crosscheck information before saving.
- Saves data in `data.json` using JSON format.
- Implements search functionality to retrieve stored credentials by website name.
- Provides error handling for missing or empty files.
- Simple and user-friendly GUI with a lock icon for added design.
- Uses Tkinter for GUI elements and MessageBox for alerts.
- Lightweight and easy to use.

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. Install the required modules if necessary (e.g., `pyperclip`).
   ```bash
   pip install pyperclip
   ```
3. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run the main script (`app.py`).
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: Double-click the script file (`app.py`) to run it, provided Python is set up to execute `.py` files on your system.

## Notes
- Data is now stored in JSON format in `data.json`, providing better structure and scalability compared to plain text files.
- If `data.json` does not exist, it will be created automatically using error handling.

## File Structure
- **`app.py`:** Main program file.
- **`experiments/`:** Folder containing temporary or practice files.
- **`screenshots/`:** Folder containing screenshots of the program.

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*
```
"""

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Method 1 for creating random password list using for loop
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    # Method 2 for creating random password list using for loop
    # password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # password_list = password_letters + password_symbols + password_numbers
    # shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_username_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password, }
    }

    # Checking if fields are empty or not
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="😿 mmm", message="Hi! Please enter all required details in fields.")
    else:
        # Asking user to cross-check the details
        # is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: "
        #                                               f"\nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        # Saving data to data.json file
        is_ok = True
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data: reading
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # Saving the updated data: writing
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.focus()
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ----------------------- SEARCH INFORMATION -------------------------- #

def search_info():
    website = website_entry.get()

    if len(website) != 0:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
                # print(data)
                # print(type(data))
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found")
        else:
            data_found = False
            for key in data:
                # This key will be website name
                if key == website:
                    data_found = True
                    email = data[key]["email"]
                    password = data[key]["password"]
                    messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            if not data_found:
                messagebox.showinfo(title=website, message=f"No data found for {website}.")
    else:
        messagebox.showinfo(title="Empty Website Field", message="Please enter something in Website field.")


# ---------------------------- UI SETUP ------------------------------- #

# Creating UI using tkinter module
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="website:", font=(FONT_NAME))
website_label.grid(column=0, row=1)

website_entry = Entry(width=31)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_label = Label(text="Email/Username:", font=(FONT_NAME))
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=53)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "@gmail.com")

name = Label(text="Create by Pranjal Sarnaik")
name.grid(column=2, row=5)

password_label = Label(text="Password:", font=(FONT_NAME))
password_label.grid(column=0, row=3)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search_info)
search_button.grid(column=2, row=1)

window.mainloop()
