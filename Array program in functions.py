from array import*
def array1():
    s=[]
    arr=array('i',[0,5,2,8,0])
    for i in arr:
        s.append(i)
        s.sort()
    print(s)    
    s.reverse()    
    print(s)
array1()    
