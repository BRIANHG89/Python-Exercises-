
#Write a Python function that takes a sequence of numbers and determines whether all the numbers
#are different from each other.

"""
list = ['a', 'e', 'i', 'o', 'u']
word=""
for i in range(len(list)):
    list.append(list.pop(0))
    print(word.join(list))
"""
a = [1,-6,4,2,-1,-2,0,0,2,-1]
x = list()
a = list(set(a)) #removes duplicates in list
for i in range(len(a)):
     for j in range(i,len(a)):
        if j==i:
            continue
        for k in range(j,len(a)):
            if k==j or k==i:
            continue
            print(i,j,k)
            if a[i]+a[j]+a[k]==0:
               x.append([a[i],a[j],a[k]])
            print(x)