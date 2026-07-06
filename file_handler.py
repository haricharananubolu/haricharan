import json
import csv
import shutil
import os
from expenses import Expense

JSON_FILE = "expenses.json"
BACKUP_FILE = "expenses_backup.json"

def save_to_json(manager):
    try:
        if os.path.exists(JSON_FILE):
            shutil.copy(JSON_FILE, BACKUP_FILE)
            
        data = {
            "expenses": [e.to_dict() for e in manager.expenses],
            "budgets": manager.budgets
        }
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except PermissionError:
        print("Permission denied: Cannot save data.")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_from_json(manager):
    if not os.path.exists(JSON_FILE):
        return
    try:
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
            manager.expenses = [Expense.from_dict(e) for e in data.get("expenses", [])]
            manager.budgets = data.get("budgets", {})
    except json.JSONDecodeError:
        print("Data file corrupted. Trying to recover from backup...")
        if os.path.exists(BACKUP_FILE):
            shutil.copy(BACKUP_FILE, JSON_FILE)
            load_from_json(manager)
    except Exception as e:
        print(f"Error loading data: {e}")

def export_to_csv(manager, filename: str):
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            for e in manager.expenses:
                writer.writerow([e.date, e.amount, e.category, e.description])
        print(f"Successfully exported data to {filename}")
    except Exception as e:
        print(f"Failed to export CSV: {e}")

def import_from_csv(manager, filename: str):
    if not os.path.exists(filename):
        print("File not found.")
        return
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if len(row) == 4:
                    try:
                        expense = Expense(row[0], float(row[1]), row[2], row[3])
                        manager.add_expense(expense)
                    except ValueError:
                        continue
        save_to_json(manager)
        print("CSV imported successfully.")
    except Exception as e:
        print(f"Error importing CSV: {e}")