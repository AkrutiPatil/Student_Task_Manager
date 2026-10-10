student = {}

while True:
    print("\n ------  Student Result Manager App ---------")
    print("1. Add Student")
    print("2. View Student")
    print("1. Check Result")
    print("1. Exit")

    choice = input("Enter your choice: ")

    #Add student
    if choice == "1":
        name = input("Enter student name : ")
        marks = int(input("Enter marks: "))
        student[name]=marks
        print(f"{name} Successfully Added")

    elif choice == "2":
        if not student:
            print("No Student Found!")
        else:
            for name, marks in student.items():
                print(name, ":" , marks)

    #check result
    elif choice == "3":
        name = input("Enter Student name:")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("Pass")

            else:
                print("Fail")

        else:
            print("Student Not Found!")

    elif choice == "4":
        print("Exiting....")
        break

    else:
        print("In-valid input")