import json
import os

data_file = 'library.json'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (Y/N): ").strip().lower() == 'y'

    new_book = {
        'title': title,
        'author': author,
        'year': int(year),
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully.")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].strip().lower() != title]
    
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found in the library.")

def search_library(library):
    while True:
        search_by = input("Search by 'title' or 'author': ").strip().lower()
        if search_by not in ["title", "author"]:
            print("Invalid choice. Please enter 'title' or 'author'.")
            continue
        break

    search_term = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if book.get(search_by, "").strip().lower() == search_term]

    if results:
        print("Books found:")
        for book in results:
            print(json.dumps(book, indent=4))
    else:
        print("No books found matching your search.")

def list_books(library):
    if not library:
        print("The library is empty.")
    else:
        print("Library Collection:")
        for book in library:
            print(json.dumps(book, indent=4))

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({percentage_read:.2f}% read)")

def main():
    library = load_library()
    while True:
        print("\nLibrary Manager")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List All Books")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            list_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Exiting Library Manager. Goodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
