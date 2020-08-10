
from array import *



array=[1,3,5,7,3,9,4,2,6,1,4,3,7,9,2,1,5,6,4,8]

count=0

print("The array is",array)
s=int(input("Enter the element you want to find the number of occurrences: "))

for i in range(0,len(array)):
   if array[i]==s:
      count=count+1

print("The Number of occurrences of the number",s,"in the said array:",count)

"""
data = array('i', [11,1,1,1,3,5,7,85])

def elCount(data, item):
    count = 0
    string = ' '
    for i in range(len(data)):
        try:
            if data[i] == data[item]:
                count += 1
        except:
            return 'The element is not in the array' 
        return 'The Element {0} appeared tiems(s) in the array'.format(item,count)
print(elCount(data,1))
"""
        