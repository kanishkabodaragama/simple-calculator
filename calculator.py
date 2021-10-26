print("Select an operation to perform:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")


operation = input()

if operation == "1":
     #code  for add
     n1=input("Enter first number:")
     n2=input("Enter second number:")
     print("Sum is"+str(int(n1)+int(n2)))
elif operation == "2":
    #sub
    
     n1=input("Enter first number:")
     n2=input("Enter second number:")
     print("Difference is"+str(int(n1)-int(n2)))
elif operation == "3":
    #mul
    
     n1=input("Enter first number:")
     n2=input("Enter second number:")
     print("Multiplication is"+str(int(n1)*int(n2)))
elif operation == "4":
    #div
    
     n1=input("Enter first number:")
     n2=input("Enter second number:")
     print("Division is"+str(int(n1)/int(n2)))
else:
     print("Invalid Entry")