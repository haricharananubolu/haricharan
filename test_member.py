from library_system.member import Member

def test_member_borrow_limits():
    m = Member("John Doe", "M01", max_limit=2)
    assert m.can_borrow() is True
    m.borrow_book("ISBN1")
    m.borrow_book("ISBN2")
    assert m.can_borrow() is False