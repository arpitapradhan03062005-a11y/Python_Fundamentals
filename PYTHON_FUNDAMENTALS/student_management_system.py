students = {}
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice :"))

    if choice == 1:
        name = input("Enter name :")
        marks = int(input("Enter marks :"))
        students.update({ name : marks })
        print("Student added!!")

    elif choice == 2:
        if len(students.items()) == 0:
            print("No student!!")
        for key,value in students.items():
            print(key , ":", value)

    elif choice == 3:
        name = input("Enter name :")
        for key,value in students.items():
            if name == key :
                print(key , ":", value)

    elif choice == 4:
        name = input("Enter name :")
        students.pop(name)
        print("Deleted successfully.")
                


    elif choice == 5:
        break

    else:
        print("Invalid choice!!")
        break
