class User:

    def __init__(self, name: str, balance: int, checking_account: bool):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount) -> str:
        """Withdraw `amount` from this account, if balance is sufficient"""
        if self.balance - amount < 0:
            raise ValueError("there isn't enough balance to withdraw amount")
        else:
            self.balance -= amount
            return f'{self.name} has {self.balance}.'


    def add_cash(self, amount) -> str:
        """Deposit `amount` into this account"""
        self.balance += amount
        return f'{self.name} has {self.balance}.'


    def check(self, issuer, amount) -> str:
        """Receive a check from `issuer` over `amount`, if possible
        `issuer` is the User issuing the check, i.e. the account the `amount` will be taken from
        `self` is the User receiving the check, i.e. the account the `amount` will be added to
        """

        if issuer.balance < amount:
            raise ValueError('baa check')
        elif not issuer.checking_account:
            raise ValueError('non-checking account')
        else:
            issuer.balance -= amount
            self.balance += amount
            return f'{self.name} has {self.balance} and {issuer.name} has {issuer.balance}.'
