import csv
"""
@author Chris Adams
Lists 
asdf

--> Mutable, ordered collection of arbitrary objects
--> Assessed by offset
--> Variable length, heterogeneous, arbitrarily nestable

"""

L = [123, 12.3, 'malware', {0:'value 0',1:'value 1', 2:'value 2'}]
print(L)
print(L[2][2],L[3])

M = [L, 2*L, 3*L]
print(M)

N = list(M)
print(N)
N = list("So if the phillies win the world series I am buying beers for everyone")
print(N)
print(N[:-50])
#O = list(range(-999999,100000))

# That made a really big list... if you want to make a really big 2 d list?
# how about

print(len(L)) # number of objects in L
print(L*3)

for index in L:
    print(index)

print(123 in L) #Boolean

L.append("string_cheese")
L.extend("alphabet")
print(L)

L.insert(4,'fawn')
print(L)
print(L.index('fawn'))

print(L.count('fawn'))
L.append('fawn')
print(L.count('fawn'))

L.clear()
print(L)
L = [123, 456, 789]

print(L)
L.pop(2) # knock one off

print(L)
L.remove(123)

print(L)
del L[0]

print(L)

L = list(range(-100, 100))
del L[10:110]

L.clear()

L = list(range(-100, 100))
print(L)

L = [x**2 for x in range(500)]
print (L)

# this line maps out the string to numeric values...
L = list(map(ord, 'bubbagump'))
print(L)


#test...

#fix this, make it part of the list

print(str([1,2]) + "34")
# this is just adding two strings, but to add to list
L.clear()
L = [1,2] + list("34")
print(L)

for x in [1,2,3]:
    print(x, end='     ')


# equivalent for loops...LIST COMPREHENSIONS
M = [c * 4 for c in 'YAY_FOR_LIST__COMPREHENSIONS']
print(M)

# an equivalent for loop would be like...

for c in 'YAY_FOR_LIST__COMPREHENSIONS':
    M.append(c*4)
print(M)


# pop all the stuff out of a list
D = [0,1,2,3,4,5,6,7,8,9,10]
while 0 in D:
    print(D.pop())

print(myList[:-4])
print(myList[:4])
print("Bubba Gump"[:5])
print("Bubba Gump"[:-5])

## Some examples of using data structures in python

i = 80 #no. of rows
j = 50 #no. of columns

# create a 1-D array that is i in dimension and fill it with equivalent numbers

# implementation using lists
myList = []
value = 1
while value <= i:
    myList.append(value)
    value = value + 1

# creating a square matrix

ROW = list(range(0,i))
TWO_D_ARR = []
for i in ROW:
    TWO_D_ARR.append(ROW)
print(TWO_D_ARR)

# what if you have 2D with difference ranks, where num of rows is different than columns


index = 0
TWO_D_ARR.clear()
while index <= j:
    TWO_D_ARR.append(ROW)
    index = index + 1

with open('lists.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(TWO_D_ARR)