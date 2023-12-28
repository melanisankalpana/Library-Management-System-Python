from bookmodel import Book

def print_info(book):
    print(f"ISBN NO: {book.isbn_no}, Title: {book.title}, Format: {book.book_format}, Subject: {book.subject}, Rental Price: {book.rental_price}, Available Copies:{book.copies}")

class BookFunction:
    """
    ATTN EVERYONE!!!!!!!
    DO ALL VALIDATION FIRST
    DO IT ON YOUR OWN RISK
    THANK YOU
    """
    def __init__(self):
        self.list_of_books = []
        self.__initial_data()

    def __initial_data(self):
        a_book1 = Book(isbn_no="ISBN0001", title="Title1", book_format="Format1", subject="Science", rental_price=12.50, copies=1)
        a_book2 = Book(isbn_no="ISBN0002", title="Title2", book_format="Format2", subject="Science", rental_price=22.50, copies=0)
        a_book3 = Book(isbn_no="ISBN0003", title="Title3", book_format="Format3", subject="Science", rental_price=32.50, copies=3)
        self.list_of_books.append(a_book1)
        self.list_of_books.append(a_book2)
        self.list_of_books.append(a_book3)

    def add(self):
        __isnb = input("Enter ISBN Number:").strip().upper()
        __title = input("title:").strip().upper()
        __book_format = input("format:")
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        a_book = Book(isbn_no=__isnb, title=__title, book_format=__book_format, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_books.append(a_book)
        print(f"Book added {a_book.isbn_no}-{a_book.title}")

    def remove(self):
        __isbn = input("Enter ISBN number:")
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            self.list_of_books.remove(x)
            print("Item Removed.")

    def lend(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies -= __copies
            print("Book Lent")

    def receive(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies += __copies
            print(f"Book Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_books:
            print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_books if x.copies > 0)
        for x in matched_data:
            print_info(book=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_books if x.copies == 0)
        for x in matched_data:
            print_info(book=x)


