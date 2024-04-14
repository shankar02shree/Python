# print 0 to 20 by using range#
print("print 0 to 20 by using range")
for num in range(0,20):
    print(num)

#print range 10 to 20#
print("\n\nprint range 10 to 20")
print(list(range(10,20)))

#Print number of items in the list by using 'len'#
print("\n\nPrint number of items in the list by using 'len'")
list=[10, 20, 14, 55, 43, 87, 76]
size=len(list)
print("Number of item in the List2: ",size)

#printing word by word from string#
print("\n\n printing word by word from string")
txt= "Artificial Intelligence"
print(txt)
for n in txt:
    print(n)


#Print this mixered datatype using Tuples#
print("\n\nPrint this mixered datatype using Tuples")
tuple=(1, 'Welcome', 2, 'Hope')
print(tuple)


#Print this nested datatype using Tuples#
print("\n\nPrint this nested datatype using Tuples")
tuple1=(0, 1, 2, 3)
tuple2=('python', 'HOPE')
tuple3=(tuple1,tuple2)
print(tuple3)

#print Odd Numbers in the list#
print("\n\nprint Odd Numbers in the list")
tuple4=(20,10,16,19,25,1,276,188)
print(tuple4)
for num in tuple4:
    if((num %2)!=0):
       print(num,"is odd")

#print Even Numbers in the list#
print("\n\nprint Even Numbers in the list")
tuple5=(20,10,16,19,25,1,276,188)
print(tuple5)
for num in tuple5:
    if((num %2)==0):
       print(num,"is even")

