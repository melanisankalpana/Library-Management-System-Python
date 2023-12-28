from Magazines import magazines


def print_info(magazie):
    print(
        f"Mag No: {magazie.mgzn_no}, Title: {magazie.title},Color:{magazie.color} Subject: {magazie.subject}, Rental Price: {magazie.rental_price}, Available Copies:{magazie.copies}")


class MagFunction:

    def __init__(self):
        self.list_of_magazines = []
        self.__initial_data()

    def __initial_data(self):
        bookA = Book(mgzn_no="01", title="History of Cricket", color="Color", subject="Sports", rental_price=12.50,
                       copies=1)
        bookB = Book(mgzn_no="02", title=", Evolution of the Computer", color="Black&White", subject="Technology", rental_price=22.50,
                       copies=0)
        bookC = Book(mgzn_no="03", title="IT Industry", color="Color", subject="IT", rental_price=32.50,
                       copies=3)
        self.list_of_magazines.append(bookA)
        self.list_of_magazines.append(bookB)
        self.list_of_magazines.append(bookC)

    def add(self):
        __magno = input("Enter Magazine Number:").strip().upper()
        __title = input("title:").strip().upper()
        __color = input("color:")
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        bookA = Book(mgzn_no=__magno, title=__title, color=__color, subject=__subject,
                      rental_price=__rental_price, copies=__copies)
        self.list_of_magazines.append(bookA)
        print(f"Magazine added {bookA.mgzn_no}-{bookA.title}")

    def remove(self):
        __magno = input("Enter Magazine number:")
        matched_data = list(x for x in self.list_of_magazines if x.mgzn_no == __magno)
        for x in matched_data:
            self.list_of_magazines.remove(x)
            print("Item Removed.")

    def lend(self):
        __magno = input("Enter Magazine number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_magazines if x.mgzn_no == __magno)
        for x in matched_data:
            x.copies -= __copies
            print("Book Lent")

    def receive(self):
        __magno = input("Enter Magazine number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_magazines if x.mgzn_no == __magno)
        for x in matched_data:
            x.copies += __copies
            print(f"Book Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_magazines:
            print_info(magazie=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_magazines if x.copies > 0)
        for x in matched_data:
            print_info(magazie=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_magazines if x.copies == 0)
        for x in matched_data:
            print_info(magazie=x)


