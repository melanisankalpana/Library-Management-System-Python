class Book:
    def __init__(self, isbn_no, title, book_format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.book_format = book_format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies