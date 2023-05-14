# u1311019
# Sejin Yoon


class Library:
    def __init__(self, acc_number, title, author):
        self.acc_number = acc_number
        self.title = title
        self.author = author

    def read(self):
        print(f"Acc Number: {self.acc_number}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def compute(self, days_late):
        fine = days_late * 1.50
        print(f"Fine charged: ${fine:.2f}")

# create a Library object with acc_number=123, title="Book Title", and author="John Doe"
book = Library(123, "Book Title", "John Doe")

# call the read method to display the book's information
book.read()

# call the compute method to calculate and display the fine for 3 days late
book.compute(3)