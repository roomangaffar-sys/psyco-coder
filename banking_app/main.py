from account import check_balance, deposit, withdraw
from bankcore import create_account, login

def main_menu():
    print('\n"Welcome to ABC Bank"')
    print("1. Create an account")
    print("2. Login to the account")
    print("3. Exit")


def banking_menu():
    print("\nBanking Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Logout")

while True:
    main_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        create_account(name, password)

    elif choice == 2:
        cid = input("Enter your customer ID: ")
        pw = input("Enter your password: ")
        if login(cid, pw):
            while True:
                banking_menu()
                option = int(input("Enter your option: "))
                if option == 1:
                    bal = check_balance(cid)
                    print("Your balance is:", bal)
                elif option == 2:
                    amt = int(input("Enter amount to deposit: "))
                    deposit(cid, amt)
                    print("Amount deposited.")
                elif option == 3:
                    amt = int(input("Enter amount to withdraw: "))
                    withdraw(cid, amt)
                elif option == 4:
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")
        else:
            print("Login failed. Try again.")

    elif choice == 3:
        print("Thank you for using ABC Bank.")
        break
    else:
        print("Invalid choice.")