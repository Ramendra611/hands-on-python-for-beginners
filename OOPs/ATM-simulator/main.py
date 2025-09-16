from atm import ATM
from bankaccount import BankAccount


"""

1. Create the bank account
2. Register the bank account with the atm
3. Ask the user to enter the account number 
4. Enter the pin
5. Authenticate and then show options
6. As per the option selected, perform deposit or withdraw
"""


def bank_session():
    atm = ATM()

    atm.register_account(BankAccount("1", 1234, 10000))
    atm.register_account(BankAccount("2", 5678, 20000))

    while True:
        account_number = input("\nEnter the account number:")
        if account_number not in atm.registered_accounts:
            print(
                "This account can't be serviced. Please try with some other account!!"
            )
            continue
        pin = int(input("Please enter your pin: "))

        try:
            account = atm.authenticate(account_number, pin)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        while True:
            atm.display_options()

            choice = input("\nEnter your choice:::")

            if choice == "1":
                balance = account.check_balance()
                print(f"Your balance:  {balance}")

            elif choice == "2":
                try:
                    withdraw_amount = int(input("Enter the amount to withdraw: "))
                    try:
                        account.withdraw(withdraw_amount)
                    except ValueError as e:
                        print(f"Error: {e}")

                except ValueError:
                    print(
                        f"Error: You have entered an invalid input. Please try again!"
                    )
                    continue

            elif choice == "3":
                try:
                    deposit_amount = int(input("Enter the amount to deposit: "))
                    try:
                        account.deposit(deposit_amount)
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                except ValueError:
                    print(
                        f"Error: You have entered an invalid input. Please try again!"
                    )
                    continue

            elif choice == "4":
                print("Thank you for banking with us! Have a nice day!!")
                break

            else:
                print("You entered an invalid option. Please try again::")
                continue


if __name__ == "__main__":
    bank_session()
