class Book:

    def __init__(self,book_id,tittle,author,available_copies):
        self.book_id = book_id
        self.title = tittle
        self.author = author
        self.available_copies = available_copies

    def display_details(self):
        print("ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available_copies}")

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        self.available_copies += 1


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user):
        self.users[user.user_id] = user

    def lend_book(self, user_id, book_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            if book.borrow_book():
                user.borrow_book(book)
                print(f"Book '{book.title}' borrowed by {user.name}.")
            else:
                print("Book is not available.")
        else:
            print("Invalid user ID or book ID.")

    def return_book(self, user_id, book_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            if book in user.borrowed_books:
                book.return_book()
                user.return_book(book)
                print(f"Book '{book.title}' returned by {user.name}.")
            else:
                print("User did not borrow this book.")
        else:
            print("Invalid user ID or book ID.")

    def display_all_books(self):
        for book in self.books.values():
            book.display_details()




library = Library()

library.add_book(Book(6,"One Piece","Luffy",8))

library.display_all_books()