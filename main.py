# e = 2.71828182846
# pi = 3.14159265


# Addition Function
def add(x, y):
  return x + y


# Subtraction Function
def subtract(x, y):
  return x - y


# Multiplication Function
def multiply(x, y):
  return x * y


# Division Function
def divide(x, y):
  return x / y


#Power Funtion
def power(x, y):
  return x**y


#sqrt Function
def sqrt(x):
  return x**0.5


print("Select operation.")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Power(**)")
print("6.Square Root(sqrt)")

while True:
  # take input from the user
  choice = input("Enter Funtion (+)(-)(*)(/)(^)(sqrt): ")

  # check if choice is one of the four options
  if choice in ('+', '-', '*', '/', '^', 'sqrt'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
      print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '-':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '*':
      print(num1, "*", num2, "=", multiply(num1, num2)) 

    elif choice == '/':
      print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '^':
      print(num1, "^", num2, "=", power(num1, num2))

    elif choice == 'sqrt':
      print('sqrt', num1, "=", sqrt(num1))

 
    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input(
      "Do you wish to do another calculation? (yes/no): ")
    if next_calculation == "no":
      break

  else:
    print("Invalid Input")
