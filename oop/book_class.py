class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize the attributes
        self.title = title
        self.author = author
        self.year = year
        print(f"Creating {self.title} by {self.author}, published in {self.year}")

    def __del__(self):
        # Destructor to print a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation for user-friendly output
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation for debugging and recreating the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
