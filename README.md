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

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/password-manager-intermediate.git
   ```

2. Navigate to the project directory:
   ```bash
   cd password-manager-intermediate
   ```

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