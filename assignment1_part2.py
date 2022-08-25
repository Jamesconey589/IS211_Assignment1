class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

if __name__ == "__main__":
    p1 = Book("John Steinbeck", "Of Mice and Men")
    p2 = Book("Harper Lee", "To Kill a Mockingbird")

    p1.display()
    p2.display()