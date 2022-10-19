from array import*
arr1=array('i',[5,6,2,0,7,9])
l=[]
for i in arr1:
    l.append(i)
    #print(i)
    l.sort()
print(l)
if sorted(l):
    print("true")
else:
    print("false")
