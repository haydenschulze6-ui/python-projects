books = {
    "Harry Potter": 5,
    "The Hobbit": 3,
    "Matilda": 4,
    "Diary of a Wimpy Kid": 2
}

late_fees = {
    "Harry Potter": 2.50,
    "The Hobbit": 1.50,
    "Matilda": 3.00,
    "Diary of a Wimpy Kid": 1.00
}

while True:
    print("\nLibrary Book Availability Checker")
    print("1. Show all books")
    print("2. Search for a book")
    print("3. Update book copies")
    print("4. Show late fees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for book, copies in books.items():
            print(book, ":", copies, "copies")

    elif choice == "2":
        name = input("Enter book name: ")
        if name in books:
            if books[name] > 0:
                print(name, "is available")
            else:
                print(name, "is unavailable")
        else:
            print("Book not found")

    elif choice == "3":
        name = input("Enter book name: ")
        if name in books:
            copies = int(input("Enter new number of copies: "))
            books[name] = copies
            print("Book copies updated")
        else:
            print("Book not found")

    elif choice == "4":
        for book, fee in late_fees.items():
            print(book, ":", fee)

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")