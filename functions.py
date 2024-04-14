#Create a class and function, and list out the items in the list
print("\n\nCreate a class and function, and list out the items in the list")

def Subfields():
    print("Sub-fields in AI are:")
    list=['Machine Learning', 'Neural Networks','Vision Robotics', 'Speech Processing', 'Natural Language Processing']
    for lst in list: 
        print(lst)
    return lst

Subfields()


## Create a function that checks whether the given number is Odd or Even
print("\n\nCreate a function that checks whether the given number is Odd or Even")

def oddEven():
    num1=int(input("Enter a number: "))
    if((num1 %2)==0):
        print(num1, "is Even number")
    else:
        print(num1, "is Odd number")

oddEven()


##Create a function that tells elegibility of marriage for male and female according to thei
##r age limit like 21 for male and 18 for female##

def Elegible():
    print("\n\nchecking the Marriage elegible")
    gender=input("Your Gender: ")
    age=int(input("Your Age: "))
    if((gender=="Male") & (age < 21)) | ((gender=="Female") & (age < 18)):
       print("You are Not eligible for Marriage")
    else:
        print("You are eligible for Marriage") 


Elegible()

#calculate the percentage of your 10th mark
print("\n\ncalculate the percentage of your 10th mark")
def percentage():
    sub1=int(input("subject1: "))
    sub2=int(input("subject2: "))
    sub3=int(input("subject3: "))
    sub4=int(input("subject4: "))
    sub5=int(input("subject5: "))
    total=sub1+sub2+sub3+sub4+sub5
    print("Total: ",total)
    per=(total/500)*100
    print("Percentage: ",per)
    return per

percentage()



##print area and perimeter of triangle using class and functions
print("\n\nprint area and perimeter of triangle using class and functions")

def triangle():
    ht=int(input("Height :"))
    brth=int(input("Breadth :"))
    af=(ht*brth)/2
    print("Area of Triangle: ",af)
    ht1=int(input("Height1:"))
    ht2=int(input("Height2:"))
    brth1=int(input("Breadth: "))
    pt=(ht1+ht2+brth1)
    print("Perimeter of Triangle: ",pt)

triangle()
