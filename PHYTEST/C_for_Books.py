from BookType import Book


def print_info(book):
    print(f"ISBN NO: {book.isbn_no}, Title: {book.title}, Format: {book.Type_format}, Subject: {book.subject}, Rental Price: {book.rppd}, Available Copies: {book.copies}")


class Codeforbooks:
    def __init__(self):
        self.BookList = []
        self.__initial_data()

    def __initial_data(self):
        book1 = Book(isbn_no="ISBN0001", title="Title1", Type_format="Format1", subject="Science", rppd=12.50, copies=1)
        book2 = Book(isbn_no="ISBN0002", title="Title2", Type_format="Format2", subject="Science", rppd=22.50, copies=0)
        book3 = Book(isbn_no="ISBN0003", title="Title3", Type_format="Format3", subject="History", rppd=32.50, copies=3)
        book4 = Book(isbn_no="ISBN0004", title="Title4", Type_format="Format4", subject="Geography", rppd=32.67, copies=1)
        book5 = Book(isbn_no="ISBN0005", title="Title5", Type_format="Format5", subject="Science", rppd=43.22, copies=2)
        self.BookList.append(book1)
        self.BookList.append(book2)
        self.BookList.append(book3)
        self.BookList.append(book4)
        self.BookList.append(book5)

    def add(self):
        __isnb = input("Enter ISBN Number:").strip().upper()
        __title = input("title:").strip().upper()
        __book_type = input("format:")
        __subject = input("Subject:")
        __rppday = float(input("rental price per day:"))
        __copies = int(input("amount of copies:"))

        book = Book(isbn_no=__isnb, title=__title, Type_format=__book_type, subject=__subject, rppd=__rppday, copies=__copies)
        self.BookList.append(book)
        print(f"Book added {book1.isbn_no}-{book1.title}")

    def remove(self):
        __isbn = input("Enter the ISBN number:")
        comparingDT = list(x for x in self.BookList if x.isbn_no == __isbn)
        for x in comparingDT:
            self.BookList.remove(x)
            print("Book Removed.")

    def lend(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("enter lend copies:"))
        comparingDT = list(x for x in self.BookList if x.isbn_no == __isbn)
        for x in comparingDT:
            x.copies -= __copies
            print("Book is Lented")

    def receive(self):
        __isbn = input("Enter ISBN number:")
        __copies = int(input("Amount of receive copies:"))
        comparingDT = list(x for x in self.BookList if x.isbn_no == __isbn)
        for x in comparingDT:
            x.No_copies += __Nocopies
            print(f"Book Received with {__Nocopies} Copies")

    def display_all(self):
        for x in self.BookList:
            print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.BookList if x.copies > 0)
        for x in comparingDT:
            print_info(book=x)

    def display_unavailable(self):
        comparingDT = list(x for x in self.BookList if x.copies == 0)
        for x in comparingDT:
            print_info(book=x)


