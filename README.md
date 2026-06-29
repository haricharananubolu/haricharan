# 📞 Contact Management System

## Week 3 Python Project - Functions & Dictionaries

### Project Description

The Contact Management System is a menu-driven Python application developed as part of the Week 3 Functions and Dictionaries project. The application helps users manage personal and professional contacts efficiently using Python dictionaries, functions, file handling, and data validation.

The project allows users to store contact details such as phone numbers, email addresses, physical addresses, and contact groups. All information is stored permanently in a JSON file so that data remains available even after closing the program.

This project demonstrates the practical implementation of Python concepts including dictionaries, nested dictionaries, functions, loops, conditional statements, regular expressions, JSON handling, CSV export, exception handling, and file operations.

---

# Project Objectives

The main objectives of this project are:

- Develop a menu-driven Contact Management System.
- Store contacts using nested dictionaries.
- Validate phone numbers and email addresses.
- Implement CRUD (Create, Read, Update, Delete) operations.
- Save and load contact information using JSON.
- Create backup files for data safety.
- Export contacts into CSV format.
- Generate contact statistics.
- Improve programming skills using Python functions and dictionaries.

---

# Features

This Contact Management System includes the following features:

### Contact Management

- Add New Contact
- Search Contact by Name
- Search Contact using Partial Name Matching
- Search Contact by Phone Number
- Update Existing Contact
- Delete Contact
- Display All Contacts

### Data Validation

- Phone Number Validation
- Email Address Validation
- Duplicate Contact Detection

### File Handling

- Save Contacts to JSON
- Load Contacts from JSON
- Automatic Backup Creation

### Advanced Features

- Contact Groups
- CSV Export
- Contact Statistics
- User-Friendly Menu Interface

---

# Technologies Used

Programming Language

- Python 3.x

Python Modules

- json
- csv
- re
- datetime
- os

These modules are built into Python, so no additional installation is required.

---

# Project Structure

```
Contact_Management_System/
│
├── contacts_manager.py
├── contacts.json
├── contacts_backup.json
├── contacts_export.csv
├── README.md
├── requirements.txt
├── test_contacts.py
└── .gitignore
```

---

# Contact Information Structure

Each contact is stored as a nested dictionary.

Example:

```python
{
    "Hari": {
        "phone": "9876543210",
        "email": "hari@gmail.com",
        "address": "Hyderabad",
        "group": "Friends",
        "created_at": "...",
        "updated_at": "..."
    }
}
```

---

# Functions Implemented

### Validation Functions

- validate_phone()
- validate_email()

### CRUD Functions

- add_contact()
- search_contacts()
- update_contact()
- delete_contact()
- display_all()

### File Functions

- save_to_file()
- load_from_file()

### Display Functions

- display_search_results()

### Advanced Functions

- search_by_phone()
- export_to_csv()
- show_statistics()

### Main Function

- main_menu()

---

# Program Workflow

1. Start the application.
2. Load existing contacts from JSON.
3. Display the Main Menu.
4. User selects an option.
5. Perform the selected operation.
6. Automatically save updated data.
7. Continue until the user exits.

---

# Menu Options

```
1. Add New Contact
2. Search Contact
3. Search by Phone Number
4. Update Contact
5. Delete Contact
6. Display All Contacts
7. Export to CSV
8. View Statistics
9. Exit
```

---

# Validation Rules

### Phone Number

- Only digits are allowed.
- Minimum length: 10 digits.
- Maximum length: 15 digits.

### Email

- Must follow standard email format.
- Example:

```
example@gmail.com
```

---

# Files Generated

The application automatically creates the following files:

### contacts.json

Stores all contact information.

### contacts_backup.json

Stores backup data before updating the main JSON file.

### contacts_export.csv

Stores exported contacts in spreadsheet format.

---

# Error Handling

The application handles several common errors such as:

- Invalid phone numbers
- Invalid email addresses
- Duplicate contact names
- Contact not found
- Invalid menu selection
- Missing JSON file
- Corrupted JSON file
- File reading and writing errors

---

# Concepts Used

This project demonstrates the following Python concepts:

- Variables
- Functions
- Dictionaries
- Nested Dictionaries
- Loops
- Conditional Statements
- Regular Expressions
- File Handling
- JSON
- CSV
- Exception Handling
- Menu-Driven Programming

---

# Advantages

- Easy to use
- Fast contact searching
- Permanent data storage
- Data backup support
- CSV export
- Input validation
- Beginner-friendly code
- Well-structured functions

---

# Future Improvements

Some additional features that can be added include:

- Password Protection
- Contact Photos
- Birthday Reminder
- GUI using Tkinter
- Database Integration using SQLite
- Search by Address
- Import Contacts from CSV
- Mobile Number Formatting
- Sorting Contacts
- Contact Favorites

---

# Requirements

Python Version

```
Python 3.10 or higher
```

Required Modules

```
json
csv
re
datetime
os
```

No external libraries are required.

---

# Author

**Name:** Hari Charan Anubolu

**Project:** Contact Management System

**Course:** Python Programming – Week 3 Project

---

# Conclusion

The Contact Management System is a complete Python application that demonstrates the effective use of functions, dictionaries, file handling, validation techniques, and modular programming. It provides a practical solution for managing contacts while helping students understand real-world software development concepts. The project is easy to use, well-organized, and can be extended with additional features in the future.