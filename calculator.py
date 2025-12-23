print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=input("Enter your choice(1/2/3/4):")
num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
if choice=='1':
  print("Result:",num1+num2)
elif choice=='2':
  print("Result:",num1-num2)
elif choice=='3':
  print("Result:",num1*num2)
elif choice=='4':
  if num2 != 0:
    print("Result:",num1/num2)
  else:
    print("Error:Division by zero is not allowed")
else:
  print("Invalid input")

