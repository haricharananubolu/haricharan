import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_system.library import Library

def print_interface():
    print("\n" + "="*45)
    print("         LIBRARY TERMINAL INTERFACE        ")
    print("="*45)
    print(" 1. Add a New Book")
    print(" 2. Register a New Member")
    print(" 3. Check Out / Borrow a Book")
    print(" 4. Return a Book")
    print(" 5. Search Book Inventory")
    print(" 6. View Library Metrics Dashboard")
    print(" 7. Run Instant Secure Database Backup")
    print(" 8. Exit System")
    print("="*45)

def main():
    lib = Library()
    
    while True:
        print_interface()
        choice = input("Enter option (1-8): ").strip()
        
        if choice == '1':
            print("\n--- Add Book ---")
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN Code: ").strip()
            year = input("Publication Year (Optional): ").strip()
            
            if not title or not author or not isbn:
                print("Error: Fields cannot be empty.")
                continue
            _, msg = lib.add_book(title, author, isbn, year if year else None)
            print(msg)
            
        elif choice == '2':
            print("\n--- Register Member ---")
            name = input("Full Name: ").strip()
            uid = input("Create Member ID: ").strip()
            
            if not name or not uid:
                print("Error: Name and ID are required.")
                continue
            _, msg = lib.register_member(name, uid)
            print(msg)
            
        elif choice == '3':
            print("\n--- Book Loan Check-Out ---")
            uid = input("Member ID: ").strip()
            isbn = input("Book ISBN: ").strip()
            _, msg = lib.library_borrow(uid, isbn)
            print(msg)
            
        elif choice == '4':
            print("\n--- Return Processing ---")
            isbn = input("Book ISBN to return: ").strip()
            _, msg = lib.library_return(isbn)
            print(msg)
            
        elif choice == '5':
            print("\n--- Search Inventory ---")
            query = input("Search keyword (Title/Author/ISBN): ").strip()
            if not query:
                continue
            results = lib.search_books(query)
            print(f"\nFound ({len(results)}) matching items:")
            for idx, item in enumerate(results, 1):
                print(f" {idx}. {item}")
                
        elif choice == '6':
            print("\n--- Library Statistics ---")
            stats = lib.get_statistics()
            for key, val in stats.items():
                print(f" * {key.replace('_', ' ').title()}: {val}")
                
        elif choice == '7':
            print("\n--- Backup Control Panel ---")
            _, msg = lib.trigger_backup()
            print(msg)
            
        elif choice == '8':
            print("\nExiting library console application. Data saved safely.")
            break
        else:
            print("Invalid input selection. Choose 1 through 8.")

if __name__ == '__main__':
    main()