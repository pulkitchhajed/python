from functions import *
while True:
    print("What do you want to do")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q or q to Exit")

    choice = input("Enter Your Choice : ")
    if choice =='Q' or choice == 'q':
        break

    num1 = int(input("Enter the Number1 : "))
    num2 = int(input("Enter the Number 2 : "))

    if choice == '1':
        Addition(num1,num2)
    elif choice == '2':
        Subtraction(num1,num2)
    elif choice == '3':
        Multiplication(num1,num2)
    elif choice == '4':
        Division(num1,num2)
    else:
        print("Invalid Choice")
    print("\n")



