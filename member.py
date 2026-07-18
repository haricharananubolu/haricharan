# member.py
class Member:
    """Represents a library member"""
    
    def __init__(self, name, member_id, max_limit=5):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # Stores list of ISBN strings
        self.max_limit = max_limit
        
    def can_borrow(self):
        """Check if member has reached their limit"""
        return len(self.borrowed_books) < self.max_limit
        
    def borrow_book(self, isbn):
        if not self.can_borrow():
            return False, f"Limit of {self.max_limit} books reached."
        if isbn in self.borrowed_books:
            return False, "Member already has this book."
            
        self.borrowed_books.append(isbn)
        return True, "Book added to member profile."
        
    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True, "Book removed from member profile."
        return False, "This book wasn't borrowed by this member."
        
    def to_dict(self):
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': self.borrowed_books,
            'max_limit': self.max_limit
        }
        
    @classmethod
    def from_dict(cls, data):
        member = cls(name=data['name'], member_id=data['member_id'], max_limit=data.get('max_limit', 5))
        member.borrowed_books = data.get('borrowed_books', [])
        return member

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) | Checked out: {len(self.borrowed_books)}/{self.max_limit}"