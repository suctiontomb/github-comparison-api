
class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        """
            Initialise a bank account.

            Args:
                owner: Name of the account holder
                balance: Starting balance, defaults to 0
            """
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount: int) -> None:
        if amount < 0:
            raise ValueError("balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount: int) -> str:
        """Deposit amount into account and returns confirmation message."""
        self. balance += amount
        return f"Amount Deposited: R{amount}. Balance: {self.balance}"

    def withdraw(self, amount: int) -> str:
        """Withdraw amount from account and returns confirmation message."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return f"Withdraw R{amount}. Balance: {self.balance}"

    def __str__(self) -> str:
        """Returns confirmation message."""
        return f"Account: {self.owner}. Balance: {self.balance}"




class SavingsAccount(BankAccount):
    def __init__(self,owner: str,balance: float,interest_rate: float) -> None:
        """
                 Initialise a savings account.

                 Args:
                     owner: Name of the account holder
                     balance: Starting balance, defaults to 0
                     interest_rate: Interest rate applied
                 """
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> str:
        """Applies interest to account and returns confirmation message."""
        self.balance += self.balance * self.interest_rate
        return f"Balance: {self.balance}> Interest rate: {self.interest_rate}"

    def __str__(self) -> str:
        """Returns confirmation message."""
        return f"{super().__str__()} Interest rate: {self.interest_rate}"


class BusinessAccount(BankAccount):
    def __init__(self,owner: str,balance: float,company_name: str) -> None:
        """
                         Initialise a Business account.

                         Args:
                             owner: Name of the account holder
                             balance: Starting balance, defaults to 0
                             company_name: Name of the company
                         """
        super().__init__(owner,balance)
        self.company_name = company_name

    def withdraw(self, amount: int) -> str:
        """Withdraw amount from account applies fee and returns confirmation message."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        fee = amount * 0.02
        self.balance -= (amount + fee)
        return f"Withdrew R{amount} + 2% fee (R{fee}). Balance: {self.balance}"

    def __str__(self) -> str:
        """Returns confirmation message."""
        return f"{super().__str__()} \n Company Name: {self.company_name}"

