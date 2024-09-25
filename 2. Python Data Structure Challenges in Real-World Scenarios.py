# 2. Python Data Structure Challenges in Real-World Scenarios

# Seems like a dictionary would be better than a tuple for this purpose.
# Also, no duplicate books doesn't make sense. Why wouldn't a library be allowed to have multiple copies of a book?
# Whatever.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_books():
    title = input("Enter the title of the book you'd like to add: ")
    book_in_library = False
    for book in library:
        if title in book:
            print("That book is already in the library.")
            book_in_library = True
        else:
            continue
    if not book_in_library:
        author = input("Enter the author's name: ")
        new_book = (title, author)
        library.append(new_book)
        print(library)

add_books()