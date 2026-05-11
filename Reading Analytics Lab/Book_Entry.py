import json
import matplotlib.pyplot as plt
books = []
def show_menu():
    print("1. Add Book")
    print("2. View Books")
    print("3. Search for Books")
    print("4. Show Summary")
    print("5. Data Visualisation")
    print("6. Exit")
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
    search_title = input ("Enter the title to search: ")
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
def show_summary():
    total_books = len(books)
    if total_books == 0:
        print ("No books added yet.")
    else:
        average_rating = sum(book['rating'] for book in books) / total_books
        print(f"Total Books: {total_books}")
        print(f"Average Rating: {average_rating:.2f}/5")
    max_genre = max(set(book['genre'] for book in books), key=lambda genre: sum(1 for book in books if book['genre'] == genre))
    print(f"Most Read Genre: {max_genre}")
    max_author = max(set(book['author'] for book in books), key=lambda author: sum(1 for book in books if book['author'] == author))
    print(f"Most Read Author: {max_author}")
    number_genre = {genre: sum(1 for book in books if book['genre'] == genre) for genre in set(book['genre'] for book in books)}
    print("Books per Genre:")
    for genre, count in number_genre.items():
        print(f"{genre}: {count}")
def show_data_menu():
    print("Create chart of:")
    print("1. Book Genre")
    print("2. Books read per month")
    print("3. Pages read per month")
    print("4. Average Rating per Genre")
    print("5. Top Authors")
    print("6. Back to Main Menu")
    data_choice = input("Please enter your choice (1-6): ")
    return data_choice
def show_genre_chart():
    genre_counts = {}
    for book in books:
        genre = book['genre']
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
    genres = list(genre_counts.keys())
    counts = list(genre_counts.values())
    plt.bar(genres, counts, color='blue')
    plt.title("Books per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Books")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def show_books_per_month():
    month_counts = {}
    for book in books:
        date_finished = book['date_finished']
        month = date_finished[:7]
        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1
    months = list(month_counts.keys())
    counts = list(month_counts.values())
    plt.plot(months, counts, marker='o', color='green')
    plt.title("Books Read per Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Books")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def show_pages_per_month():
    month_pages = {}
    for book in books:
        date_finished = book['date_finished']
        month = date_finished[:7]
        pages = book['number_of_pages']
        if month in month_pages:
            month_pages[month] += pages
        else:
            month_pages[month] = pages
    months = list(month_pages.keys())
    pages = list(month_pages.values())
    plt.plot(months, pages, marker='o', color='red')
    plt.title("Pages Read per Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Pages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def show_average_rating_per_genre():
    genre_ratings = {}
    genre_counts = {}
    for book in books:
        genre = book['genre']
        rating = book['rating']
        if genre in genre_ratings:
            genre_ratings[genre] += rating
            genre_counts[genre] += 1
        else:
            genre_ratings[genre] = rating
            genre_counts[genre] = 1
    genres = list(genre_ratings.keys())
    average_ratings = [genre_ratings[genre] / genre_counts[genre] for genre in genres]
    plt.bar(genres, average_ratings, color='purple')
    plt.title("Average Rating per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def show_top_authors():
    author_counts = {}
    for book in books:
        author = book['author']
        if author in author_counts:
            author_counts[author] += 1
        else:
            author_counts[author] = 1
    top_authors = sorted(author_counts.items(), key=lambda item: item[1], reverse=True)[:5]
    authors = [author for author, count in top_authors]
    counts = [count for author, count in top_authors]
    plt.bar(authors, counts, color='orange')
    plt.title("Top Authors")
    plt.xlabel("Author")
    plt.ylabel("Number of Books Read")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
books = load_books()
print("================== Reading Analytics Lab ==================")
print("Welcome to the Reading Analytics Lab!")
print("This program helps you track your reading habits and analyze your reading data.")
while True:
    show_menu()
    choice = input("Please enter your choice (1-5): ")
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
        save_books()
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
        show_summary()
    elif choice == "5":
        data_choice = show_data_menu()
        if data_choice =="1":
            show_genre_code()
        elif data_choice == "2":
            show_books_per_month()
        elif data_choice == "3":
            show_pages_per_month()
        elif data_choice == "4":
            show_average_rating_per_genre()
        elif data_choice == "5":
            show_top_authors()
        elif data_choice == "6":
            continue
        else:
            print("Invalid choice. Please try again.")
            break
    elif choice == "6":
        print ("You chose to exit")
        break

    else:
        print ("Invalid choice. Please try again.")
