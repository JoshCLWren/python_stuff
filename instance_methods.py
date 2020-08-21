# Adding instance methods

class User:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age

  def full_name(self):
    return f"{self.first} {self.last}"

  def initials(self):
    return f"{self.first[0]}.{self.last[0]}."

  def likes(self, thing):
    return f"{self.first} likes {thing}"

  def is_senior(self):
    return self.age >= 65

  def birthday(self):
    self.age += 1
    return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 40)

print(user1.full_name())
print(user1.initials())
print(user1.likes("candy"))
print(user1.age)
print(user1.is_senior())
print(user1.birthday())
print(user1.age)

class BankAccount:
  def __init__(self, owner, balance=0.0):
    self.owner = owner
    self.balance = balance

  def deposit(self, debit):
    self.balance = debit + self.balance
    return self.balance

  def withdraw(self, deficit):
    self.balance = self.balance - deficit
    return self.balance




acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)