class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def __str__(self):
        return self.title + " by " + self.author


book1 = Book("Harry Potter", "J.K. Rowling")
print(book1)
book1.borrow()
book1.return_book()