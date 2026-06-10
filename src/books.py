books = []

def add_book(book_name, read_status = False):
    if not book_name:
        raise ValueError("Book name cannot be empty")
    elif book_name in [book["book name"] for book in books]:
        raise ValueError(f"Book '{book_name}' already exists in the list.")
    else:
        books.append({"book name": book_name, "read status": read_status})
        return f"Book '{book_name}' added with read status 'Unread'."
    
def mark_as_read(book_name):
    for book in books:
        if book["book name"] == book_name:
            book["read status"] = True
            return f"Book '{book_name}' marked as read."
    raise ValueError(f"Book '{book_name}' not found in the list.")

def list_books():
    if books == []:
        return "No books in the list."
    else:
        for book in books:
            print(f"Book: {book['book name']}, Read Status: {book['read status']}")

def book_page(page_number):
    if page_number < 1:
        raise ValueError("Page number out of range")
    else:
        return f"Page {page_number} exists in the book."
    
def delete_book(book_name):
    for book in books:
        if book["book name"] == book_name:
            del books[books.index(book)]
            return f"Book '{book_name}' deleted from the list."
    else: 
        raise ValueError(f"Book '{book_name}' not found in the list. Deleting nothing.")
    
def filter_books_by_read_status(read_status):
    filtered_books = [book for book in books if book["read status"] == read_status]
    if not filtered_books:
        return f"No books with read status '{read_status}' found."
    else:
        return filtered_books
    
def clear_books():
    books = []
    return f"all books cleared from the list. {books}"