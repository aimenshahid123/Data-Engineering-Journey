choice = 0
name = input("Enter your Name :")
age = int(input("Enter your age : "))
while choice != 4:
    
    print("="*35)
    print ("MAIN MENU".center(35))
    print("="*35)
    print("1. Say Hello")
    print("2. Show name")
    print("3. Show age")
    print("4.Exit")

    choice = int(input("Enter your choice between 1 and 4:"))

    if choice == 1:
        print(f"Hello {name} :)")
    elif choice == 2:
        print(f"Your name is {name}")
    elif choice == 3:
        print(f"Your age is {age}")

    elif choice == 4:
        print("Good Bye :)")
    else:
        print("Invalid Choice.")
    print()