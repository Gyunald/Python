class Account :
    num_accounts = 0
    def __init__(self, name) :
        self.name = name
        Account.num_accounts += 1
    def __del__(self) :
        Account.num_accounts -= 1
kim = Account("kim")
Lee = Account("Lee")
print(kim.name)
print(Lee.name)
print(kim.num_accounts)
print(Lee.num_accounts)
print(Account.num_accounts)