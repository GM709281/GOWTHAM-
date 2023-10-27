class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited ${amount}. New balance is ${self.__account_balance:.2f}")
      else:
          print("Invalid deposit amount. Please enter a positive amount.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrew ${amount}. New balance is ${self.__account_balance:.2f}")
      else:
          print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
      print(f"Account Holder: {self.__account_holder_name}")
      print(f"Account Number: {self.__account_number}")
      print(f"Account Balance: ${self.__account_balance:.2f}")

# Example usage
if __name__ == "__main__":
  account = BankAccount("123456", "John Doe", 1000.0)
  account.display_balance()
  account.deposit(500.0)
  account.withdraw(200.0)
  account.display_balance()
