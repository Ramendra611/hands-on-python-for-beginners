from bankaccount import BankAccount


class ATM:
    """
    ATM class that will register an account, authenticate and then allow the user to depost or withdraw money
    from the account.
    """

    def __init__(self):
        self.registered_accounts = {}

    def register_account(self, account: BankAccount):

        self.registered_accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.registered_accounts.get(account_number)
        if not account:
            raise ValueError("Account not found!! Please try again!!")
        if pin == account.pin:
            print("Login successful!!")
            return account
        else:
            raise ValueError("INVALID PIN!")

    @staticmethod
    def display_options():
        print(
            """
                Select the correct option:
                    1. Check your balance
                    2. Withdraw 
                    3. Deposit
                    4. Exit

        """
        )
