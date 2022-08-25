class Budget:
    
    def __init__(self, category):
        self.category = category
        self.total = 0
        self.ledger = [] 

    def __repr__(self):
        header = self.category.center(30,'*')
        print(header)
        for item in self.ledger:
            amount = '%.2f' % item['amount']
            desc = (item['description'][:28 - (len(amount))] + '..') if len(item['description']) > 28 - (
                len(amount)) else item['description']
            spaces = " " * (30 - (len(desc) + len(amount)))
            txt = f'{desc:<}{spaces}{amount:>}'
            print(txt)
        x = ("Total: " + '%.2f' % self.total)
        return x

    def deposit(self, amount, description = ""):
        self.total += amount
        self.ledger.append({'amount' : amount, 'description' : description})

    def withdraw(self, amount, description = ""):
        if self.check_funds:
            self.total -= amount
            self.ledger.append({'amount' : -amount, 'description' : description})
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, instance):
        if self.check_funds:
            self.total -= amount
            self.ledger.append({'amount': amount, 'description': 'Transfer to ' + instance.category})

            instance.total += amount
            instance.ledger.append({'amount': amount, 'description': 'Transfered from ' + self.category})
        else:
            return False

    def check_funds(self, amount):
        if amount < self.total:
            return True
        else:
            return False


food = Budget('food')
car = Budget('car')
food.deposit(600, 'initial check')
food.deposit(650)
food.withdraw(2000, 'celebration meal')
food.transfer(500, car)
print(food.__repr__())
print(car.__repr__())
