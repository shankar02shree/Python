
#1printng statement
print("Welcome to Assignment-1")

#2Adding the values
Num1=10
Num2=30
print("Num1=",Num1)
print("Num2=",Num2)
print("Add=",Num1+Num2)


#3 BMI calculation
bmi=float(input("Enter the BMI index: "))
if(bmi<18.5):
    print("Under Weight")
elif(bmi<24.9):
    print("Normal Weight")
elif(bmi<29.9):
    print("Over Weight")
else:
    print("Very Overweight")
