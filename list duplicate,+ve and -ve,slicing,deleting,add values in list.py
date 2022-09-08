#list which type of operations are accessable
#1)list allowes duplicate values
a=[10,20,30,10,20,30,50]
print(a)

#list is acceptable -ve and +ve values:
b=[10,-20,60,-50,10]
print(b)

#list index values +ve and -ve values:
c=[10,20,30,40,50]
print(a[0])
print(a[-1])

# list allowes slicing operation:(slicing operation always left to right)
d=[2,3,5,8,9]
print(d[0:3])
print(d[-5:-1])
print(d[2:])
print(d[:])
print(d[:5])
print(d[0:6:3])

#deleting list values and adding values:
e=[1,2,3,4,5,6,7]
print(e)
e[0]=0
print(e)
del e[2]
print(e)




