from random import random

N=20

array=[]

for x in range(N):
    array.append(int(random()*100))

array.sort()
print(array)

number = int(input("Search for any number in the array: "))

minimum = 0
maximum =  N-1

while minimum <= maximum:
    mid = (minimum + maximum) // 2
    if number < array[mid]:
        maximum = mid-1
    elif number > array[mid]:
        minimum = mid+1
    else:
        print("The number is located at index: ", mid)
        break
else:
    print("There is no number!")




