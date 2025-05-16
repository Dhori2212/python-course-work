class Book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        

    def display_details(self):
        print("----- Book Details -----")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Publisher : {self.publisher}")
        print(f"Price     : ₹{self.price}")
        print("------------------------")


# Example usage
book1 = Book(
    title="The Alchemist",
    author="Paulo Coelho",
    publisher="HarperCollins",
    price=3900
)

book1.display_details()
