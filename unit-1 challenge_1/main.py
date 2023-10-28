fact = 1
num = int(input("Enter a number:"))
if (num == 0):
  print("The factorial of 0 is 1")
else:
  for i in range(1, num + 1):
    fact = fact * i
  print("The Factorialof", num, "is", fact)
