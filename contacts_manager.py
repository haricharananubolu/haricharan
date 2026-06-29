# contacts_manager.py
# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime
import csv
import os

# Step 1: Define file path constants for storage
DATA_FILE = "contacts.json"
BACKUP_FILE = "contacts_backup.json"

# ==========================================
# STEP 2: Core Data Structure & Helpers
# ==========================================

def validate_phone(phone):
    """Validate phone number format (Keep 10-15 digits)"""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    """Validate email format using basic regex pattern"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ==========================================
# STEP 3: CRUD Functions
# ==========================================

def add_contact(contacts):
    """Add a new contact to the dictionary with full validation"""
    print("\n--- ADD NEW CONTACT ---")
    
    # Get contact name
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update instead? (y/n): ").lower()
                if choice == 'y':
                    update_contact(contacts, name)
                    return contacts
                else:
                    return contacts
            break
        print("Name cannot be empty!")
    
    # Get phone number with validation
    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid:
            break
        print("Invalid phone number! Please enter 10-15 digits.")
    
    # Get email with validation
    while True:
        email = input("Enter email (optional, press Enter to skip): ").strip()
        if not email or validate_email(email):
            break
        print("Invalid email format!")
    
    # Get additional info
    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"
    
    # Store in nested dictionary
    contacts[name] = {
        'phone': cleaned_phone,
        'email': email if email else None,
        'address': address if address else None,
        'group': group.capitalize(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    print(f"✅ Contact '{name}' added successfully!")
    save_to_file(contacts)  # Auto-save changes
    return contacts

def search_contacts(contacts, search_term=None):
    """Search contacts by name (partial match)"""
    if not search_term:
        search_term = input("\nEnter name or partial name to search: ").strip()
        
    search_term = search_term.lower()
    results = {}
    
    for name, info in contacts.items():
        if search_term in name.lower():
            results[name] = info
            
    display_search_results(results)
    return results

def update_contact(contacts, name=None):
    """Modify an existing contact's details"""
    print("\n--- UPDATE CONTACT ---")
    if not name:
        name = input("Enter the name of the contact to update: ").strip()
        
    if name not in contacts:
        print("❌ Contact not found.")
        return contacts
        
    info = contacts[name]
    print(f"Updating profile details for: {name}")
    print("(Press Enter to skip modifying a specific field)")
    
    # Update Phone
    new_phone = input(f"Enter new phone [{info['phone']}]: ").strip()
    if new_phone:
        while True:
            is_valid, cleaned_phone = validate_phone(new_phone)
            if is_valid:
                info['phone'] = cleaned_phone
                break
            print("Invalid phone number format! Must be 10-15 digits.")
            new_phone = input(f"Enter new phone [{info['phone']}]: ").strip()
            if not new_phone: break

    # Update Email
    new_email = input(f"Enter new email [{info['email'] or 'None'}]: ").strip()
    if new_email:
        while True:
            if validate_email(new_email):
                info['email'] = new_email
                break
            print("Invalid email format!")
            new_email = input(f"Enter new email [{info['email'] or 'None'}]: ").strip()
            if not new_email: break

    # Update Address
    new_address = input(f"Enter new address [{info['address'] or 'None'}]: ").strip()
    if new_address:
        info['address'] = new_address
        
    # Update Group Designation
    new_group = input(f"Enter new group [{info['group']}]: ").strip()
    if new_group:
        info['group'] = new_group.capitalize()
        
    info['updated_at'] = datetime.now().isoformat()
    print(f"✅ Contact '{name}' updated successfully!")
    save_to_file(contacts)
    return contacts

def delete_contact(contacts):
    """Delete a contact with structural confirmation checking"""
    print("\n--- DELETE CONTACT ---")
    name = input("Enter the exact name of the contact to delete: ").strip()
    
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}' permanently? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            del contacts[name]
            print(f"✅ Contact '{name}' deleted successfully.")
            save_to_file(contacts)
        else:
            print("Deletion canceled.")
    else:
        print("❌ Contact not found.")
    return contacts

def display_all(contacts):
    """Display all contacts inside the application matching structured ordering"""
    print("\n--- DISPLAY ALL CONTACTS ---")
    if not contacts:
        print("Your contact book is empty.")
        return
    display_search_results(contacts)

# ==========================================
# STEP 4: File Operations & Persistence
# ==========================================

def save_to_file(contacts, filename=DATA_FILE):
    """Save contacts to JSON file and implement backup functionality"""
    try:
        # Step 4 Feature: Automated backup rotation before rewriting files
        if os.path.exists(filename):
            os.replace(filename, BACKUP_FILE)
            
        with open(filename, 'w') as f:
            json.dump(contacts, f, indent=4)
    except IOError as e:
        print(f"⚠️ Error protecting configuration records: {e}")

def load_from_file(filename=DATA_FILE):
    """Load contacts from JSON file or hot-restore via fallback backup asset"""
    if not os.path.exists(filename):
        if os.path.exists(BACKUP_FILE):
            print("⚠️ Primary storage file corrupt or missing. Restoring via backup registry map...")
            filename = BACKUP_FILE
        else:
            return {}
            
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Corrupt stream encountered on boot profile check. Resetting clean collection.")
        return {}

# ==========================================
# STEP 5: User Interface Layout
# ==========================================

def display_search_results(results):
    """Display search results or collections in a formatted way"""
    if not results:
        print("No records matched or found.")
        return
    
    print(f"\nShowing {len(results)} profile(s):")
    print("-" * 50)
    
    for idx, (name, info) in enumerate(sorted(results.items()), 1):
        print(f"{idx}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        if info.get('email'):
            print(f"   📧 Email: {info['email']}")
        if info.get('address'):
            print(f"   📍 Address: {info['address']}")
        print(f"   👥 Group: {info['group']}")
        print(f"   🕒 Last Modified: {info['updated_at'][:10]}")
        print("-" * 30)

# ==========================================
# STEP 6: Advanced Features
# ==========================================

def search_by_phone(contacts):
    """Implement search by phone number substring matching"""
    print("\n--- SEARCH BY PHONE NUMBER ---")
    phone_term = input("Enter part of the phone number to search: ").strip()
    phone_term = re.sub(r'\D', '', phone_term) # Keep digits only
    
    if not phone_term:
        print("❌ Invalid input digits pattern.")
        return
        
    results = {name: info for name, info in contacts.items() if phone_term in info['phone']}
    display_search_results(results)

def export_to_csv(contacts):
    """Add export to CSV file functionality"""
    print("\n--- EXPORT DATABASE TO CSV ---")
    if not contacts:
        print("❌ No profiles available in current stack to extract.")
        return
        
    filename = input("Enter destination file name [Default: contacts_export.csv]: ").strip() or "contacts_export.csv"
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # CSV Headers
            writer.writerow(['Contact Name', 'Phone', 'Email', 'Address', 'Category Group', 'Created On', 'Updated On'])
            for name, info in contacts.items():
                writer.writerow([
                    name, 
                    info['phone'], 
                    info.get('email', ''), 
                    info.get('address', ''), 
                    info['group'], 
                    info['created_at'], 
                    info['updated_at']
                ])
        print(f"✅ Database exported successfully to CSV spreadsheet asset: '{filename}'")
    except IOError as e:
        print(f"❌ Spreadsheet generation failure: {e}")

def show_statistics(contacts):
    """Create statistics summary report mapping metrics data"""
    print("\n--- CONTACT BOOK METRICS ---")
    total = len(contacts)
    print(f"Total Profiles Saved: {total}")
    
    if total == 0:
        return
        
    group_counts = {}
    for info in contacts.values():
        g = info.get('group', 'Other')
        group_counts[g] = group_counts.get(g, 0) + 1
        
    print("\nVolume Breakdown by Group Category:")
    for group, count in group_counts.items():
        print(f" 🔹 {group}: {count} contact(s) ({count/total*100:.1f}%)")

# ==========================================
# STEP 5 & 7: UI Controller Loop
# ==========================================

def main_menu():
    """Main dashboard menu configuration routing logic"""
    # Load system dictionary metrics upon launch sequence initialization
    contacts = load_from_file()
    
    while True:
        print("\n==================================")
        print("    CONTACT MANAGEMENT SYSTEM    ")
        print("==================================")
        print("1. Add New Contact Record")
        print("2. Search Contacts by Name Syntax")
        print("3. Reverse Search via Phone Digits")
        print("4. Update Contact Profile Details")
        print("5. Delete Contact Record Profile")
        print("6. Display Master Directory List")
        print("7. Export System Database to CSV")
        print("8. View Database Storage Analytics")
        print("9. Terminate Application Pipeline")
        print("==================================")
        
        choice = input("Select option index (1-9): ").strip()
        
        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            search_by_phone(contacts)
        elif choice == '4':
            contacts = update_contact(contacts)
        elif choice == '5':
            contacts = delete_contact(contacts)
        elif choice == '6':
            display_all(contacts)
        elif choice == '7':
            export_to_csv(contacts)
        elif choice == '8':
            show_statistics(contacts)
        elif choice == '9':
            print("\nFlushing cache data maps safely down. Application closed. Goodbye!")
            break
        else:
            print("❌ Input selection out of operational index space. Enter an integer digit (1-9).")

if __name__ == "__main__":
    main_menu()



           


     