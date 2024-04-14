# print 'CORRECT' if i == 10
print("print 'CORRECT' if i == 10")
i=int(input("value: "))
if(i==10):
    print("CORRECT")


#Check the password, using if and else
print("Check the password, using if and else")
pwd=input("Enter the password: ")
if(pwd=='HOPE@123'):
    print("Your password is correct")
else:
    print("Your password is incorrect")


#Catagory the people by their age like children, adult, citizen, senior citizen...
print("Catagory the people by their age like children, adult, citizen, senior citizen..")
age=int(input("Age: "))
if(age<18):
    print("Children")
elif(age<35):
    print("Adult")
elif(age<59):
    print("Citizen")
else:
    print("Senior Citizen")


# Find whether given number is positive or negative
print("Find whether given number is positive or negative")
Num1=int(input("Enter any number: "))
if(Num1 > 0):
    print("Given Number is Positive")
else:
    print("Given Number is negative")


#Check whether the given number is divisible by 5
print("Check whether the given number is divisible by 5")
Num2=int(input("Enter a number to check: "))
if (Num2%5==0):
    print("Given No is divisible by 5")
else:
    print("Given No is not divisible by 5")
    