import json
books = []
def show_menu():
    print("1. Add Book")
    print("2. View Books")
    print("3. Search for Books")
    print("4. Exit")
def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file)
def search_menu():
    print("Search by:")
    print("1. Author")
    print("2. Genre")
    print("3. Title")
    print("4. Back to Main Menu")
    search_choice = input("Please enter your choice (1-4): ")
    return search_choice
def search_books_author():
    search_author = input ("Enter the author's name to search: ")
    found_books = [book for book in books if book['author'].lower() == search_author.lower()]
    if not found_books:
        print ("No books found by that author.")
    else:
        for book in found_books:
            print(f"Title: {book['title']}")
            print(f"Genre: {book['genre']}")
            print(f"Pages: {book['number_of_pages']}")
            print(f"Started: {book['date_started']}")
            print(f"Finished: {book['date_finished']}")
            print(f"Rating: {book['rating']}/5")
            print()
def search_books_genre():
    search_genre = input ("Enter the genre to search: ")
    found_books = [book for book in books if book['genre'].lower() == search_genre.lower()]
    if not found_books:
        print ("No books found in that genre.")
    else:
        for book in found_books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Pages: {book['number_of_pages']}")
            print(f"Started: {book['date_started']}")
            print(f"Finished: {book['date_finished']}")
            print(f"Rating: {book['rating']}/5")
            print()
def search_books_title():
    found_books = [book for book in books if book['title'].lower() == search_title.lower()]
    if not found_books:
        print ("No books found with that title.")
    else:
        for book in found_books:
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Pages: {book['number_of_pages']}")
            print(f"Started: {book['date_started']}")
            print(f"Finished: {book['date_finished']}")
            print(f"Rating: {book['rating']}/5")
            print()
books = load_books()
print("================== Reading Analytics Lab ==================")
print("Welcome to the Reading Analytics Lab!")
print("This program helps you track your reading habits and analyze your reading data.")
while True:
    show_menu()
    choice = input("Please enter your choice (1-3): ")
    if choice == "1":
        print ("You chose to add a book")
        title = input ("Enter the book's title: ")
        author = input ("Enter the book's author: ")
        genre = input ("Enter the book's genre: ")
        number_of_pages = int(input ("Enter the number of pages in the book: "))
        date_started = input ("Enter the date you started reading the book (YYYY-MM-DD): ")
        date_finished = input ("Enter the date you finished reading the book (YYYY-MM-DD): ")
        rating = int(input ("Enter your rating for the book (1-5): "))
        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "number_of_pages": number_of_pages,
            "date_started": date_started,
            "date_finished": date_finished,
            "rating": rating
        }
        books.append(book)
        books = save_books()
        print ("Book added successfully!")
    elif choice == "2":
        print ("You chose to view the books")
        if not books:
            print ("No books added yet.")
        else:
            for index, book in enumerate(books):
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Genre: {book['genre']}")
                print(f"Pages: {book['number_of_pages']}")
                print(f"Started: {book['date_started']}")
                print(f"Finished: {book['date_finished']}")
                print(f"Rating: {book['rating']}/5")
                print()
    elif choice == "3":
        search_choice = search_menu()
        if search_choice == "1":
            search_books_author()
        elif search_choice == "2":
            search_books_genre()
        elif search_choice == "3":
            search_books_title()
        elif search_choice == "4":
            continue
        else:
            print("Invalid choice. Please try again.")
            break

    elif choice == "4":
        print ("You chose to exit")
        break

    else:
        print ("Invalid choice. Please try again.")