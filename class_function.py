class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        list=['Machine Learning', 'Neural Networks','Vision Robotics', 'Speech Processing', 'Natural Language Processing']
        for lst in list: 
            print(lst)
        return lst


class OddEven():
    def oddEven():
        print("\n\n")
        num1=int(input("Enter a number: "))
        if((num1 %2)==0):
            print(num1, "is Even number")
        else:
            print(num1, "is Odd number")


class ElegiblityForMarriage():
    def Elegible():
        print("\n\nchecking the Marriage elegible")
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if((gender=="Male") & (age < 21)) | ((gender=="Female") & (age < 18)):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE") 


class FindPercent():
    def percentage():
        print("\n\ncalculate the percentage of your 10th mark")
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


class triangle():  
    def triangle():
        print("\n\nprint area and perimeter of triangle using class and functions")
        ht=int(input("Height :"))
        brth=int(input("Breadth :"))
        af=(ht*brth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",af)
        ht1=int(input("Height1:"))
        ht2=int(input("Height2:"))
        brth1=int(input("Breadth: "))
        pt=(ht1+ht2+brth1)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",pt)

