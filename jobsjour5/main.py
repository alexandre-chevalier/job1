#jobs 1 
"""
def fruits():
    fruits = ["pomme","cerise","orange"]
    return print(fruits)
fruits()
"""
#jobs 2
"""
def fruits():
    fruits = ["pomme","cerise","orange"]
    return print(fruits[1])
fruits()
"""
#jobs 3
"""
fruit = input("rentrez un fruit : ")

def fruits(frui):

    fruits = ["pomme","cerise","orange"]
    fruits.append(frui)
    return print(fruits)
fruits(fruit)

"""
#jobs 4
"""
fruit = input("rentrez un fruit : ")

def fruits(frui):

    fruits = ["pomme","cerise","orange"]
    fruits.insert(2, frui)
    return print(fruits)

fruits(fruit)
"""
#jobs 5
"""
L= [1,2,3,4,5]

print(L[1])

def list(L):
    print(L)
    L[3]= L[2]+ L[4]
    print(L)
list(L)
"""

#jobs 6
"""
L= [1,2,3,4,5]

print(L[1])

def list(L):
    print(L)
    l= L[0]
    L[0] = L[4]
    L[4] = l
    print(L)
list(L)

"""
#jobs 7
"""
L = [8,24,48,2,16]
l = []
for chiffre in L:
    if chiffre %  3 == 0:
        l.append(chiffre)
        

print(len(l))    

"""

#jobs 8
"""
L = [8,24,27,48,2,16,9,7,84,91]
l = []
for chiffre in L:
    if chiffre %  2 == 0:
        l.append(chiffre)
        

print(sum(l))

"""
#jobs 9
"""
L = [8,24,27,48,2,16,9,102,7,84,91]
print(min(L))
print(max(L))
"""
#jobs 10
"""
L = [8,24,27,48,2,16,9,7,84,91]
l = []
i =1
for chiffre in L:
    if chiffre>=25 and chiffre<=90 :
        l.append(chiffre)

for val in l:
    i = i * val

print(l)
print(i)
"""
#jobs 11
"""
L = [7, 11, 42, 39, 2]
L=[x+1 for x in L]
print(L)

"""
#jobs 12
L =[15,451,32,45,98,1,75]

def croissant(list):
    for i in range (0, L)
        print
croissant(L)