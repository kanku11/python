#calculator
import math
#Add
def addnum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a+b)

#Multiply
def mulnum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))    
    print(a*b)

#Subtract
def subnum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a-b)

#Divide(q)
def divnum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a/b)

#Modulus(rem)
def modnum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a%b)
 
#Power(exponent)
def pownum():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(pow(a,b))

if __name__ == "__main__":
  
#loop to run the app
  print("claculator here :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Subtraction")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Exit")
#user's choice
  
    choice = input("Enter your choice: ")

    if (choice == "1"):
         addnum()
    elif (choice == "2"):
         mulnum()
    elif (choice == "3"):
       subnum()
    elif (choice == "4"):
       divnum
    elif (choice == "5"):
       modnum()
    elif (choice == "6"):
       pownum()
    elif (choice == "7"):
            break
    else:
      print("Invalid input. Please try again.")

  print("bye! 👋👋")
