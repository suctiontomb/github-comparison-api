from models.bank_account import BankAccount

def save_account(account: BankAccount) -> list | str:
    """Save a bank account to accounts.txt file."""
    with open("accounts.txt","a") as f:
        f.write(f"{account.owner}, {account.balance}\n")
    return f"Account saved"

def load_accounts() -> str:
    """Read and print all accounts from accounts.txt."""
    with open("accounts.txt", "r") as f:
        contents = f.read()
        print(contents)
    return f"Accounts fetched"

def reconstruct_accounts() -> list[BankAccount]:
    """Read accounts.txt and return a list of BankAccount objects."""
    accounts = []
    with open("accounts.txt","r") as f:
        for line in f:
            temp = line.split(", ")
            accounts.append(BankAccount(temp[0],int(temp[1].strip())))
    return accounts

import json
def save_accounts_json(account:BankAccount) -> None:
    """Save a bank account to accounts.json file."""
    try:
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
    except FileNotFoundError:
        accounts = []

    accounts.append({"owner": account.owner, "balance": account.balance})

    with open("accounts.json","w") as f:
        json.dump(accounts,f)


def load_accounts_json() -> list[BankAccount]:
    """Read accounts.json and return a list of BankAccount objects."""
    result = []
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
        for i in accounts:
            result.append(BankAccount(i["owner"], i["balance"]))
    return result
