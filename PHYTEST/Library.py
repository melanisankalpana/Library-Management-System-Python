print("=== Open University Library Management System ===")
print(" Main Menu ")
print(" ---------- ")

print("Select What you want:")
print("-------------------")
resources = ["Books", "Magazines", "Educational DVDs", "Lecture CDs"]
for i, resource in enumerate(resources):
    print(f"{i+1} - {resource}")

    menu_items = ["Books", "Magazines", "Educational DVDs", "Lecture CDs"]
    for m, item in enumerate(menu_items, start=1):
        print(f"{m}. {item}")
    menu_choice = int(input("Type Menu Item Number: "))
    print(f"You selected: {menu_items[menu_choice - 1]}")

    if menu_choice == 1:
        print("\nBook Menu:\n")
        # Add your book-related code here

        def display_menu(self):
            print(f"\n{self.name} Library Menu:\n")
            print("1 - Add a Book")
            print("2 - Remove a Book")
            print("3 - Display Available Book")
            print("4 - Display Unavailable Book")
            print("5 - Lend Book")
            print("6 - Receive Book")
            print("7 - Back to Main Menu")
            print("0 - Quit")

    # submenu for books
    class Library:
        books = []

        def __init__(self, name):
            self.name = name

        def display_menu(self):
            print(f"\n{self.name} Library Menu:\n")
            print("1 - Add a Book")
            print("2 - Remove a Book")
            print("3 - Display Available Book")
            print("4 - Display Unavailable Book")
            print("5 - Lend Book")
            print("6 - Receive Book")
            print("7 - Back to Main Menu")
            print("0 - Quit")

        def add_book(self, book):
            self.books.append(book)
            print(f"\n{book.title} has been added to the library.")

        def remove_book(self, book):
            if book in self.books:
                self.books.remove(book)
                print(f"\n{book.title} has been removed from the library.")
            else:
                print(f"\n{book.title} is not in the library.")

        def display_available_books(self):
            print("\nAvailable Books:")
            for book in self.books:
                if book.num_copies > 0:
                    print(book)

        def display_unavailable_books(self):
            print("\nUnavailable Books:")
            for book in self.books:
                if book.num_copies == 0:
                    print(book)

        def lend_book(self, book):
            if book in self.books:
                if book.num_copies > 0:
                    book.num_copies -= 1
                    print(f"\n{book.title} has been lent out.")
                else:
                    print(f"\n{book.title} is not available for lending.")
            else:
                print(f"\n{book.title} is not in the library.")

        def receive_book(self, book):
            if book in self.books:
                book.num_copies += 1
                print(f"\n{book.title} has been received.")
            else:
                print(f"\n{book.title} is not in the library.")




