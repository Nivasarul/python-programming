def add(x, y):
   return x + y
def sub(x, y):
   return x - y
def mul(x, y):
   return x * y
def div(x, y):
   return x / y
def greaterthan(x, y):
   return x > y
def mod(x, y):
   return x % y
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation.")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.greaterthan")
print("6.mod")
choice = input("Enter choice(1/2/3/4/5/6): ")
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", mul(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", div(num1,num2))
elif choice == '5':
   print(num1,">",num2,"=", greaterthan(num1,num2))
elif choice == '6':
   print(num1,"%",num2,"=", mod(num1,num2))
else:
   print("Invalid input")
