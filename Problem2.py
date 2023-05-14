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