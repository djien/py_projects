num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(num1, " + ", num2, " = ", num1+num2)

## Extra stuff starts here ##

def cal(num_a,num_b,op):
  if op == "+":
   return num_a + num_b
  elif op == "-":
   return num_a - num_b
  elif op == "*":
   return num_a * num_b
  elif op == "/":
   return num_a / num_b
  elif op == "%":
   return num_a % num_b
  else: print("invalid input")

print("")
print("<Two Numbers Operation>")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
#Take two numbers and adds them together
print(num1, " + ", num2, " = ", num1+num2)
#Take two numbers and subtract the second from the first number
print(num1, " - ", num2, " = ", num1-num2)
#Take two numbers and multiply the two
print(num1, " * ", num2, " = ", num1*num2)
#Take two numbers and divide the first number by the second number
print(num1, " / ", num2, " = ", num1/num2)
#Take two numbers and perform a modulus operation
print(num1, " % ", num2, " = ", num1%num2)
print("")
 
#Allow users to choose which operation they want to perform on two numbers.
op1 = input("Pick an operation [+, -, *, /, %]: ")
 
if op1 == "+":
 print(num1, op1, num2, " = ", cal(num1,num2,op1)) 
elif op1 == "-":
  print(num1, op1, num2, " = ", cal(num1,num2,op1))
elif op1 == "*":
  print(num1, op1, num2, " = ", cal(num1,num2,op1))
elif op1 == "/":
  print(num1, op1, num2, " = ", cal(num1,num2,op1))
elif op1 == "%":
  print(num1, op1, num2, " = ", cal(num1,num2,op1))
else:
  print("invalid input")
print("")

 #Take 3 numbers and add them together
print("<Sum of Three Numbers>")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
number = [num1,num2,num3]
print(num1, " + ", num2, " + ", num3, " = ", sum(number)) 
print("")

 #Allow users to mix operations with 3 numbers or more
print("<Three Numbers Operation>")
num1 = int(input("First number: "))
op1 = input("First operation [+, -, *, /, %]: ")
num2 = int(input("Second number: "))
op2 = input("Second operation [+, -, *, /, %]: ")
num3 = int(input("Third number: "))

if (op2 in ["*","/","%"] ) and (op1 in ["+","-"]):
  total = cal(num2,num3,op2)
  print(num1,op1,num2,op2,num3," = ",cal(num1, total,op1))
else:
  total = cal(num1,num2,op1)
  print(num1,op1,num2,op2,num3," = ",cal(total,num3,op2))
print("")
print("Thank you for playing!")
