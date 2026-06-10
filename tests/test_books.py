import pytest
from books import add_book, mark_as_read, list_books, delete_book, filter_books_by_read_status, clear_books

def test_add_book():
    assert add_book("Foundation") == "Book 'Foundation' added with read status 'Unread'."
    assert add_book("Dune") == "Book 'Dune' added with read status 'Unread'."
    with pytest.raises(ValueError):
        add_book("")

def test_mark_as_read():
    add_book("Foundation")
    add_book("Dune")
    assert mark_as_read("Foundation") == "Book 'Foundation' marked as read."
    assert mark_as_read("Dune") == "Book 'Dune' marked as read."
    with pytest.raises(ValueError):
        mark_as_read("Nonexistent Book")

def test_list_books():
    add_book("Foundation")
    add_book("Dune")
    list_books()

def test_delete_book():
    add_book("Foundation")
    add_book("Dune")
    assert delete_book("Foundation") == "Book 'Foundation' deleted from the list."
    with pytest.raises(ValueError):
        delete_book("Nonexistent Book")
    
def test_duplicate_book():
    add_book("Foundation")
    with pytest.raises(ValueError):
        add_book("Foundation")

def test_filter_books_by_read_status():
    add_book("Foundation", read_status=True)
    add_book("Dune", read_status=False)
    assert filter_books_by_read_status(True) == [{"book name": "Foundation", "read status": True}]
    assert filter_books_by_read_status(False) == [{"book name": "Dune", "read status": False}]
    assert filter_books_by_read_status("Nonexistent Status") == "No books with read status 'Nonexistent Status' found."

def test_clear_books():
    add_book("Foundation")
    add_book("Dune")
    assert clear_books() == f"all books cleared from the list. {[]}"