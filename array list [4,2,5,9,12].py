from array import*
def get(arr):
    #arr=[4,2,5,9,12]
    a=arr[0:2]
    print(a)
    b=arr[2:4]
    print(b)
    for i in arr:
        if i==12:
            a.append(i)
        elif i==4:
            b.append(i)
    print(a)
    print(b)
    print(sum(a))
    print(sum(b))
get([4,2,5,9,12])
