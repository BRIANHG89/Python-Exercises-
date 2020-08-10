from array import *

#program to reverse the order of the items in the array 
#[1,3,5,3,7,1,9,3]


array_num = array('i', [1,3,5,3,7,1,9,3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items")
print(str(array_num))