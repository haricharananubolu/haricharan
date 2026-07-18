from library_system.book import Book

def test_book_creation():
    book = Book("1984", "George Orwell", "12345")
    assert book.title == "1984"
    assert book.available is True

def test_checkout_process():
    book = Book("1984", "George Orwell", "12345")
    success, msg = book.check_out("MEM01")
    assert success is True
    assert book.available is False
    assert book.borrowed_by == "MEM01"