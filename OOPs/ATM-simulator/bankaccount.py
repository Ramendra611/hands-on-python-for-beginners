class BankAccount:

    def __init__(self, account_number: str, pin: int, balance: float):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount: float):
        # todo: check if amount is positive
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Amount {amount} deposited!! You new balance is : {self.balance}")
            # todo: add logs for this
        else:
            raise ValueError("Amount to be deposited can't be negative")

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(
                    f"Amount {amount} withdrawn!! You new balance is : {self.balance}"
                )
            else:
                raise ValueError("Insuffient balance!!")

        else:
            raise ValueError("Amount to be withdrawn can't be negative")
