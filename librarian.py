import uuid
import requests

class Book(object):
    """An object representation of a book.
    Returns a librarian.Book type"""

    def __init__(self):
        """Initial value.
        No return."""

        self.id = uuid.uuid4()
        self.title = "Untitled"
        self.author = ["Unknown"]
        self.length = 0
        self.content = "Blank"

    def assign_id(self):
        """Assigns a book a unique id.
        Returns a uuid."""

        self.id = uuid.uuid4()
        return self.id

    def assign_title(self, title):
        """Assigns a book a title.
        Returns a string of the book title."""

        self.title = str(title)
        return self.title

    def assign_author(self, author):
        """Assign a book one more author.
        Returns a list of authors."""

        self.author = [str(x) for x in self.author if x != "Unknown"]
        self.author.append(str(author))
        return self.author

    def assign_length(self, pageCount):
        """Assigns a book a length.
        Returns an int of book length."""

        self.length = int(pageCount)
        return self.length

    def assign_content(self, bookURL="https://raw.githubusercontent.com/shakna-israel/NecromancersApprentice/master/docs/000-Chapter-Zero.md"):
        """Assigns a book some content from a given URL.
        Returns a string of content."""

        self.content = requests.get(str(bookURL)).text
        return self.content

class Series(object):
"""An object representation of a group of books.
Returns a librarian.Series type."""

    def __init__(self):
        """Inital values.
        No return."""

        self.books = {}

    def add_book(self, book):
        """Add a book to a series.
        Returns a single key/value pair of uuid to title."""
 
        self.books[book.id] = book.title
        return self.books[book.id]

    def get_titles(self):
        """Get the titles of the books in the Series.
        Returns a list of titles."""

        return self.books.items()
