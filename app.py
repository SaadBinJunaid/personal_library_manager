import re
import datetime
import sys

# Define the empty list where all books are stored
library = []

# Define the menu function
def show_menu():
    while True:
        print("\n📚 Welcome to Your Personal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_Statistics()
        elif choice == "6":
            print("Goodbye! Exiting the program.")
            sys.exit()  # 🛑 Completely stops the program
        else:
            print("❌ Invalid choice. Please choose a valid option.")

# Function to add a book
def add_book():
    print("\n📖 Add a New Book")

    # Validate book title
    while True:
        title = input("Enter the title of the book: ").strip().title()                
        if re.search(r"[a-zA-Z]", title):
            break
        else:
            print("❌ Invalid input! Title must contain letters.")

    # Validate author name
    while True:
        author = input("Enter the author of the book: ").strip().title()
        if re.search(r"[a-zA-Z]", author):
            break
        else:
            print("❌ Invalid input! Author must contain letters.")

    # Validate year (must be a number)
    current_year = datetime.datetime.now().year
    while True:
        year = input(f"Enter the year of the book between 1000 and {current_year}: ").strip()
        if year.isdigit() and 1000 <= int(year) <= current_year:  # Ensures only numbers are accepted
            year = int(year)
            break
        else:
            print(f"❌ Invalid input! Year must be a number between 1000 and {current_year}.")

    # Validate genre
    while True:
        genre = input("Enter the genre of the book: ").strip().title()
        if re.search(r"[a-zA-Z]", genre):
            break
        else:
            print("❌ Invalid input! Genre must contain letters.")

    # Validate read status
    while True:
        read = input("Have you read this book? (yes/no/maybe): ").strip().lower()
        if read in ["yes", "no","maybe"]:
            break
        else:
            print("❌ Invalid input! Please enter yes or no or maybe.")

    # Create book dictionary
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    
    # check if this book is already in you library 
    for existing_book in library:

        if (existing_book["title"].lower() == title.lower() and 
            existing_book["author"].lower() == author.lower() and
            existing_book["year"] == year and
            existing_book["genre"].lower() == genre.lower()):
            print(f"❌ '{title}' by {author} ({year}, {genre}) is already in your library!")
            return

    # Add book to the library
    library.append(book)
    print(f"\n✅ '{title}' by {author} has been added successfully!")

def remove_book():
    if not library:
        print("❌ The library is empty! Please add a book first.")
        return
    
    print("\n📖 Books in Your Library:")
    for index, book in enumerate(library,start=1):
        print(f"{index}- {book['title']} by {book['author']} ({book['year']} - Read: {book['read'].capitalize()})")

    search_query = input("Enter the title or author name of the book to remove: ").strip().lower()
   
     # Find all books with the matching title
    matching_books = [book for book in library if search_query in book["title"].lower() or search_query in book["author"].lower()]
    
    if not matching_books:
        print("❌ No book found matching your search query. ")
        return
    
    # If only one match, delete it directly
    if len(matching_books) == 1:
        library.remove(matching_books[0])
        print(f"✅ '{matching_books[0]['title']}' has been removed successfully!")
        return
    
    # Inform the user about the number of matches and also if one book is found the say book if 2 or 3 books found the say books.
    print(f"\n📖 Found {len(matching_books)} book(s) matching your search query. '{search_query}'")
    
    for index, book in enumerate(matching_books,start=1):
        print(f"- {index}. {book['title']} by {book['author']} ({book['year']}, {book['genre']} - Read: {book['read'].capitalize()}) ")
            
    # If multiple matches, ask the user to choose
    while True:
        try:
            choice = int(input(f"\nEnter the number (1-{len(matching_books)}) of the book to remove: (e.g., {matching_books[0]['title']} by {matching_books[0]['author']}): "))
            if 1 <= choice <= len(matching_books):
                book_to_remove = matching_books[choice - 1]  # Get selected book
                library.remove(book_to_remove)  # Remove it from the main list
                print(f"✅ '{book_to_remove['title']}' by {book_to_remove['author']} has been removed successfully!")
                return
            else:
                print("❌ Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            
def search_books():
    if not library:
        print("❌ The library is empty! Please add a book first,then search it.")
        return
    search_book = str(input("search books by title or author name: ")).strip().lower()
    matching_books = [book for book in library if search_book in book["title"].lower() or search_book in book["author"].lower()]
    
    if not matching_books:
        print("❌ No book found with this query ")
        return
    print(f"\n📖Books Found: ")
    for index, book in enumerate(matching_books,start=1):
        print(f"{index}- {book['title']} by {book['author']} ({book['year']} - Read: {book['read'].capitalize()})")

def display_books():
    if not library:
        print("❌ The library is empty! Please add a book first.")
        return
    
    print("\n📖 Books in Your Library:")
    for index, book in enumerate(library,start=1):
        print(f"{index}- {book['title']} by {book['author']} ({book['year']} - Read: {book['read'].capitalize()})")
        
def display_Statistics():
    if not library:
        print("❌ The library is empty! Please add a book first.")
        return
    
    # Count the total number of books
    Total_Books = len(library)
    
    # Count how many books the user has read
    read_books = sum(1 for book in library if book["read"] == "yes")  
    
    # Count how many books the user hasn't read
    unread_books = sum(1 for book in library if book["read"] == "no")
    
    # Count books marked as "maybe" read
    maybe_books = sum(1 for book in library if book["read"] == "maybe")
    
    # Find the oldest and newest book by comparing years
    oldest_book =min(library, key=lambda book: book["year"])
    newest_book = max(library, key=lambda book: book["year"])
    
    # Print the statistics
    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {Total_Books}")
    print(f"✅ Books Read: {read_books}")
    print(f"❌ Books Unread: {unread_books}")
    print(f"🤔 Maybe Read: {maybe_books}")
    print(f"📅 Oldest Book: {oldest_book['title']} ({oldest_book['year']}) by {oldest_book['author']}")
    print(f"📅 Newest Book: {newest_book['title']} ({newest_book['year']}) by {newest_book['author']}")


# ✅ Start the program
show_menu()
