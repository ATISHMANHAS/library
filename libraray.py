import csv

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def display_details(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.available_copies}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}'.")


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user):
        self.users[user.user_id] = user

    def save_to_csv(self, books_file="books.csv", users_file="users.csv"):
        with open(books_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Title", "Author", "Available Copies"])
            for book in self.books.values():
                writer.writerow([book.book_id, book.title, book.author, book.available_copies])

        with open(users_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["User ID", "Name", "Borrowed Books"])
            for user in self.users.values():
                borrowed_books_ids = ",".join(str(book.book_id) for book in user.borrowed_books)
                writer.writerow([user.user_id, user.name, borrowed_books_ids])

        print(f"Library data saved to '{books_file}' and '{users_file}'.")

    def load_from_csv(self, books_file="books.csv", users_file="users.csv"):
        try:
            with open(books_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        int(row["Book ID"]),
                        row["Title"],
                        row["Author"],
                        int(row["Available Copies"]),
                    )
                    self.add_book(book)

            with open(users_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(int(row["User ID"]), row["Name"])
                    borrowed_books_ids = row["Borrowed Books"].split(",") if row["Borrowed Books"] else []
                    for book_id in borrowed_books_ids:
                        if int(book_id) in self.books:
                            user.borrow_book(self.books[int(book_id)])
                    self.add_user(user)

            print(f"Library data loaded from '{books_file}' and '{users_file}'.")
        except FileNotFoundError as e:
            print(f"File not found: {e}. Starting fresh!")


library = Library()
book1 = Book(2, "God of War", "Kratos", 8)
book2 = Book(3, "Red Dead Redemption", "Arthur Morgan", 7)
library.add_book(book1)
library.add_book(book2)
user1 = User(1, "Alice")
user2 = User(2, "Bob")
library.add_user(user1)
library.add_user(user2)
user1.borrow_book(book1)
library.save_to_csv()
new_library = Library()
new_library.load_from_csv()
for book in new_library.books.values():
    book.display_details()
for user in new_library.users.values():
    print(f"User {user.name} has borrowed {[b.title for b in user.borrowed_books]}")
