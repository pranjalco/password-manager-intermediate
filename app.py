from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

"""
# Password Manager
A Password Manager with a GUI to store, manage, and retrieve passwords securely. It generates random passwords, copies them to the clipboard, and stores credentials in a JSON file with search and validation features.  

## Screenshots
![ss1](./screenshots/1.png), ![ss2](./screenshots/2.png)

## Author
Pranjal Sarnaik

## Features
- Generates strong random passwords.  
- Automatically copies passwords to the clipboard.  
- Validates input to ensure no fields are empty.  
- Saves credentials in `data.json` and allows searching.  
- Simple GUI with a lock icon for design appeal.  

## Level
Intermediate

## Tech Stack
Python | Tkinter | JSON | File Handling | Clipboard Handling | Error Handling

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/password-manager-intermediate.git

2. Run(Also install required libraries):
    ```bash  
   pip install pyperclip
   python app.py
"""

FONT_NAME = "Courier"

def clean_up():
    website_entry.focus()
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")
    email_username_entry.delete(0, "end")
    email_username_entry.insert(0, "@gmail.com")

# ------------------------------------------ PASSWORD GENERATOR ------------------------------------------ #


def generate_password():
    """This function generates strong password"""
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

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ------------------------------------------ SAVE PASSWORD ------------------------------------------ #


def save():
    website = website_entry.get().strip().title()
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
                clean_up()


# ------------------------------------------ SEARCH INFORMATION ------------------------------------------ #

def search_info():
    website = website_entry.get().strip().title()

    if len(website) != 0:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)

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

# ------------------------------------------ DELETE INFORMATION ------------------------------------------ #

def delete_info():
    website = website_entry.get().strip().title()

    if len(website) != 0:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found.")
        else:
            data_found = False
            if website in data:
                data_found = True
                confirmation = messagebox.askyesno(
                    title="Confirm delete", 
                    message="Are you sure you want to delete this entry?"
                    )
                if confirmation:
                    data.pop(website, None)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)

                    clean_up()
            if not data_found:
                messagebox.showinfo(title=website, message=f"No data found for '{website}'.")
    else:
        messagebox.showinfo(title="Empty Website Field", message="Please enter website name in website field.")


# ------------------------------------------ UI SETUP ------------------------------------------ #

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

delete_button = Button(text="Delete", width=15, command=delete_info)
delete_button.grid(column=2, row=2)

window.mainloop()
