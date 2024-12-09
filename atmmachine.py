balance = 1000.00

def display_menu():
    print("Welcome to the ATM")
    print("What are you here for today?")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

while True:
    display_menu()
    choice = input("Choose a number from (1-4): ")

    if choice == "1":
        print(f"Your current Balance is {balance:.2f}")

    elif choice == "2":
        try:
            depositing = float(input("Ammount to Deposit: $"))
            if depositing > 0:
                balance += depositing
                print(f"Your new balance is:{balance:.2f} ")
            else:
                print("Please Enter a right ammount greater than 0")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "3":
        try:
            withdrawing = float(input("How much would you like to withdraw: $"))
            if withdrawing > balance:
                print("You dont have enough balance")
            else:
                balance -= withdrawing
                print(f"Your new balance is:{balance: .2f}")
        except ValueError:
            print("Invalid input, Please Enter a right ammount")
    elif choice == "4":
        print("\nThank you for using the ATM. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please select from 1 to 4.")
