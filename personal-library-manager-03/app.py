import json
import os

# Load library from file safely
def load_library(filename="library.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = file.read().strip()
                if data:
                    return json.loads(data)
            except json.JSONDecodeError:
                print("⚠️ Warning: Couldn't decode the file. Starting with an empty library.")
    return []

# Save library to file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

# Show menu
def display_menu():
    print("\n📚 Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book to library
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for books by title or author
def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search term: ").strip().lower()
    matches = []

    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("\n🔍 Matching Books:")
        for i, book in enumerate(matches, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("❌ No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("📭 Your library is empty.")
        return
    print("\n📖 Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Show library stats
def display_stats(library):
    total = len(library)
    if total == 0:
        print("📊 No books in library.")
        return
    read_books = sum(1 for book in library if book['read'])
    percent_read = (read_books / total) * 100
    print(f"📚 Total books: {total}")
    print(f"📘 Percentage read: {percent_read:.1f}%")

# Main program
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

