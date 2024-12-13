class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"название книги: {self.title}, автор: {self.author}, год издания: {self.year}"


book1 = Book(input(), input(), input())
info = book1.get_info()
print(info)
