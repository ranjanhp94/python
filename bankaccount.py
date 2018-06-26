class BankAccount(object):

  def __init__(self, name):
    self.name = name
    self.balance = 0

  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    print "%s's account. Balance: $%.2f" % (self.name, self.balance)

  def deposit(self, amount):
    if amount <= 0:
     print "Some deposit issue"
     return
    else:
     print "%s's account. Balance: $%.2f" % (self.name, self.balance)
    self.balance += amount
    self.show_balance()

  def withdraw(self, amount):
    if amount >= self.balance:
      print "Amount withdraw more than current balance"
      return
    else:
     print "%s's account. Balance: $%.2f" % (self.name, self.balance)
    self.balance -= amount
    self.show_balance()

my_account = BankAccount("Ranjan")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(500)
print my_account
