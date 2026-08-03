

books = {
    "Python": 5,
    "AI": 3
}

while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Exit")

    choice = int(input("Enter choice :"))
    if choice == 1:
        name = input("Enter book name :")
        if name not in books.keys():
            books.update({name : 1})
            print("Book added!!")
        else:
            books[name] += 1
    
    elif choice == 2:
        if books == {}:
            print("No books available")
        else:
            for key,value in books.items():
                print(key , ":", value)

    elif choice == 3:
            name = input("Enter book name :")
            if name in books.keys():
                print(name,books.get(name))
            else:
                print("Book not found!!")

    elif choice == 4:
        name = input("Enter book name :")
        if name in books:

            if books[name] > 0:
                books[name] -= 1
                print("Book Borrowed!")

            else:
                print("Book not available!")

        else:
            print("Book not found!")

    elif choice == 5:
        break

    else:
        print("Invalid choice!")
    

