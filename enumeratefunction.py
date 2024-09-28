
#Enumerate functions in python

name = 'saugat'
index = 0
for char in name:
    print(char)
    if (index == 3):
        print("this is the third index")
    index += 1

'''
The upper method is common method, to use enumerate fuction it is mentioned below
'''

for newindex , char in enumerate(name):
    print(newindex,char)



fruits = ['apple', 'banana', 'mango']
#we can also change the index so the index of apple becomes 2, followed by banana 3 and mango=4
for index,fruit in enumerate(fruits, start=2):
    print(fruit, index)