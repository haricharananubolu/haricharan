import os
from library_system.library import Library

def test_library_operations(tmpdir):
    lib = Library(data_dir=str(tmpdir))
    lib.add_book("Test Title", "Test Author", "999")
    lib.register_member("Alice", "A01")
    
    success, msg = lib.library_borrow("A01", "999")
    assert success is True
    assert lib.books["999"].available is False