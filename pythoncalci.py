#Making a simple calculator using python code:-

#The function adds the two numbers:-
def add(a,b):
    return a+b
#The function subtracts the two numbers:-
def subtract(a,b):
    return a-b
#The function multiplies the two numbers:-
def multiply(a,b):
    return a*b
#The function divides the two numbers:-
def divide(a,b):
    return a/b


#Instructs the user to get answer for the given question:-
print("Select the operations:")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")


while True:
#Getting the user input:-
    choice = input("Enter the operation [1/2/3/4] :")

#Checking whether it goes through one of these operations:-
    if choice in ('1','2','3','4'):
       num1 = float(input("Enter the first number:"))
       num2 = float(input("Enter the second number:"))
    
       if choice == '1':
          print(num1, "+", num2, "=", add(num1,num2))

       elif choice == '2':
          print(num1, "-", num2, "=", subtract(num1,num2))

       elif choice == '3':
          print(num1, "*", num2, "=", multiply(num1,num2))

       elif choice == '4':
          print(num1, "/", num2, "=", divide(num1,num2))
       
#If user input operation is incorrect:-       
    else:
          print("Invalid Input") 

#To continue more:-
    New_calculation = input("Let's try another = [y/n]")
    if New_calculation == "n":
      break














