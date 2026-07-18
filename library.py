import json
import os
import shutil
from datetime import datetime
from library_system.book import Book
from library_system.member import Member

class Library:
    """Manages system database processes, collections, updates and backups"""
    
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.books_file = os.path.join(data_dir, 'books.json')
        self.members_file = os.path.join(data_dir, 'members.json')
        self.backup_dir = os.path.join(data_dir, 'backup')
        
        self.books = {}    
        self.members = {}  
        
        os.makedirs(self.backup_dir, exist_ok=True)
        self.load_data()
        
    def add_book(self, title, author, isbn, year=None):
        if isbn in self.books:
            return False, "A book with this ISBN already exists."
        self.books[isbn] = Book(title, author, isbn, year)
        self.save_data()
        return True, f"Successfully added: {title}"
        
    def remove_book(self, isbn):
        if isbn not in self.books:
            return False, "Book not found."
        if not self.books[isbn].available:
            return False, "Cannot remove a book that is currently out on loan."
        del self.books[isbn]
        self.save_data()
        return True, "Book removed successfully."
        
    def register_member(self, name, member_id):
        if member_id in self.members:
            return False, "Member ID already registered."
        self.members[member_id] = Member(name, member_id)
        self.save_data()
        return True, f"Successfully registered: {name}"

    def library_borrow(self, member_id, isbn):
        if isbn not in self.books:
            return False, "Book not found."
        if member_id not in self.members:
            return False, "Member not found."
            
        book = self.books[isbn]
        member = self.members[member_id]
        
        if not member.can_borrow():
            return False, "Member has reached their borrowing limit."
            
        success, message = book.check_out(member_id)
        if not success:
            return False, message
            
        member.borrow_book(isbn)
        self.save_data()
        return True, f"Success! Checked out '{book.title}' to {member.name}."

    def library_return(self, isbn):
        if isbn not in self.books:
            return False, "Book not found."
            
        book = self.books[isbn]
        if book.available:
            return False, "This book isn't currently checked out."
            
        member_id = book.borrowed_by
        member = self.members.get(member_id)
        
        days_late = book.days_overdue()
        book.return_book()
        if member:
            member.return_book(isbn)
            
        self.save_data()
        if days_late > 0:
            return True, f"Returned '{book.title}'. It was {days_late} days overdue."
        return True, f"Returned '{book.title}' successfully."

    def search_books(self, query):
        query = query.lower()
        return [b for b in self.books.values() if query in b.title.lower() or query in b.author.lower() or query == b.isbn]

    def get_statistics(self):
        total = len(self.books)
        available = sum(1 for b in self.books.values() if b.available)
        return {
            "total_books": total,
            "available_books": available,
            "borrowed_books": total - available,
            "total_members": len(self.members)
        }

    def trigger_backup(self):
        """Creates a stamped copies archive snapshot folder"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        dest_folder = os.path.join(self.backup_dir, f"backup_{timestamp}")
        os.makedirs(dest_folder, exist_ok=True)
        
        try:
            if os.path.exists(self.books_file):
                shutil.copy(self.books_file, os.path.join(dest_folder, 'books.json'))
            if os.path.exists(self.members_file):
                shutil.copy(self.members_file, os.path.join(dest_folder, 'members.json'))
            return True, f"Backup successfully executed inside: backup_{timestamp}"
        except IOError as e:
            return False, f"Backup execution error: {e}"

    def save_data(self):
        try:
            with open(self.books_file, 'w') as f:
                json.dump({isbn: b.to_dict() for isbn, b in self.books.items()}, f, indent=4)
            with open(self.members_file, 'w') as f:
                json.dump({m_id: m.to_dict() for m_id, m in self.members.items()}, f, indent=4)
        except IOError as e:
            print(f"Error saving data tracking records: {e}")

    def load_data(self):
        try:
            if os.path.exists(self.books_file):
                with open(self.books_file, 'r') as f:
                    data = json.load(f)
                    self.books = {isbn: Book.from_dict(b_dict) for isbn, b_dict in data.items()}
            if os.path.exists(self.members_file):
                with open(self.members_file, 'r') as f:
                    data = json.load(f)
                    self.members = {m_id: Member.from_dict(m_dict) for m_id, m_dict in data.items()}
        except (json.JSONDecodeError, IOError):
            print("Database files not found or blank. Initializing an empty system.")