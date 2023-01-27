class Banking:
    def __init__(self, name, amount):
        """
        :param name: To create your account using your username
        :param amount: At first deposit in your account
        """
        self.name = name
        self.amount = amount

    def deposit(self, tk):
        """
        :param tk: If you want to deposit your money and finally you deposit something its already added to your main amount
        :return:
        """
        self.amount += tk
        return self.amount
    def withdraw(self, tk):
        """
        :param tk: If you want to withdraw your money and when you withdraw your money and its automatically less your main account
        :return:
        """
        self.amount -= tk
        return self.amount


name = input("User name: ")
amount = int(input("Deposit: "))
person = Banking(name, amount)
print(f'Congress! Hi {person.name} You are create an account')
transaction = input('Do you create any transaction at the moment? ')
if transaction == 'yes' and 'Yes':
    print('Check your transactions')
    Which = input("Deposit or Withdraw:")
    if Which == 'deposit' and 'Deposit':
        tk = int(input("Place your amount: "))
        total = str(person.deposit(tk))
        print(f'{person.name} your total amount is {total}')
    elif Which == 'withdraw' and 'Withdraw':
        tk = int(input('Place your amount: '))
        total = str(person.withdraw(tk))
        print(f'{person.name} your total balance is {total}')
    else:
        print("Your passing wrong information, pls provide right information")
else:
    print('Thank for your responding')

print(dir(name))
