from DVDS import DVD


def print_info(DVDS):
    print(
        f"ISBN NO: {DVDS.dvd_no}, Title: {DVDS.title}, Subject: {DVDS.subject}, Rental Price: {DVDS.rental_price}, Available Copies:{DVDS.copies}")


class DvdFunction:

    def __init__(self):
        self.list_of_DVD = []
        self.__initial_data()

    def __initial_data(self):
        a_book1 = DVD(dvd_no="ISBN0001", title="Title1", subject="Science", rental_price=12.50,
                       copies=1)
        a_book2 = DVD(dvd_no="ISBN0002", title="Title2", subject="Science", rental_price=22.50,
                       copies=0)
        a_book3 = DVD(dvd_no="ISBN0003", title="Title3", subject="Science", rental_price=32.50,
                       copies=3)
        self.list_of_DVD.append(a_book1)
        self.list_of_DVD.append(a_book2)
        self.list_of_DVD.append(a_book3)

    def add(self):
        __isnb = input("Enter DVD Number:").strip().upper()
        __title = input("title:").strip().upper()
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        a_book = Book(dvd_no=__isnb, title=__title, subject=__subject,
                      rental_price=__rental_price, copies=__copies)
        self.list_of_DVD.append(a_book)
        print(f"Book added {a_book.isbn_no}-{a_book.title}")

    def remove(self):
        __isbn = input("Enter DVD number:")
        matched_data = list(x for x in self.list_of_DVD if x.isbn_no == __isbn)
        for x in matched_data:
            self.list_of_DVD.remove(x)
            print("Item Removed.")

    def lend(self):
        __isbn = input("Enter DVD number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_DVD if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies -= __copies
            print("DVD Lent")

    def receive(self):
        __isbn = input("Enter DVD number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_DVD if x.isbn_no == __isbn)
        for x in matched_data:
            x.copies += __copies
            print(f"DVD Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_DVD:
            print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_books if x.copies > 0)
        for x in matched_data:
            print_info(book=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_books if x.copies == 0)
        for x in matched_data:
            print_info(book=x)


