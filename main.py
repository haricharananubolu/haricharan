from expenses import Expense, ExpenseManager
import file_handler
import reports

def get_input(prompt: str, validator_func) -> str:
    while True:
        data = input(prompt).strip()
        try:
            return validator_func(data)
        except ValueError as e:
            print(f"Input Error: {e}")

def display_expenses(expenses):
    if not expenses:
        print("No records found.")
        return
    print(f"\n{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 65)
    for idx, e in enumerate(expenses):
        print(f"{idx:<5} | {e.date:<12} | {e.category:<15} | ${e.amount:<9.2f} | {e.description}")

def main():
    manager = ExpenseManager()
    file_handler.load_from_json(manager)
    
    while True:
        print("\n===== EXPENSE TRACKER MENU =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Search Expenses")
        print("5. Set Category Budget")
        print("6. View Reports & Predictions")
        print("7. Export to CSV")
        print("8. Import from CSV")
        print("9. Exit")
        
        choice = input("Select an option (1-9): ").strip()
        
        if choice == "1":
            date = get_input("Enter date (YYYY-MM-DD): ", Expense.validate_date)
            amount_str = get_input("Enter amount: ", Expense.validate_amount)
            category = get_input("Enter category: ", lambda x: Expense.validate_string(x, "Category"))
            desc = get_input("Enter description: ", lambda x: Expense.validate_string(x, "Description"))
            
            exp = Expense(date, float(amount_str), category, desc)
            alert = manager.add_expense(exp)
            file_handler.save_to_json(manager)
            print(alert)
            
        elif choice == "2":
            display_expenses(manager.expenses)
            
        elif choice == "3":
            display_expenses(manager.expenses)
            if manager.expenses:
                try:
                    idx = int(input("\nEnter ID to delete: "))
                    if manager.remove_expense(idx):
                        file_handler.save_to_json(manager)
                        print("Expense removed successfully.")
                    else:
                        print("Invalid ID.")
                except ValueError:
                    print("Please enter a valid numeric ID.")
                    
        elif choice == "4":
            query = input("Enter keyword search string: ")
            cat_filter = input("Filter by specific category? (Leave blank for all): ").strip()
            cat_filter = cat_filter if cat_filter else None
            results = manager.search_expenses(query, cat_filter)
            display_expenses(results)
            
        elif choice == "5":
            category = input("Enter category name: ").strip()
            try:
                amt = float(input(f"Set maximum monthly budget for {category}: "))
                manager.set_budget(category, amt)
                file_handler.save_to_json(manager)
                print(f"Budget for {category} set to ${amt:.2f}")
            except ValueError:
                print("Invalid budget input amount.")
                
        elif choice == "6":
            if not manager.expenses:
                print("No records available to analyze.")
                continue
            reports.generate_monthly_summary(manager)
            reports.generate_category_breakdown(manager)
            reports.generate_trend_analysis(manager)
            
        elif choice == "7":
            filename = input("Enter destination CSV file name (e.g., export.csv): ").strip()
            file_handler.export_to_csv(manager, filename if filename else "export.csv")
            
        elif choice == "8":
            filename = input("Enter source CSV file path: ").strip()
            file_handler.import_from_csv(manager, filename)
            
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice selection. Try again.")

if __name__ == "__main__":
    main()