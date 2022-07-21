x=int(input("Enter any value of x:"))
n=int(input("Enter the no.of terms:"))
ex=0
for i in range(1,n):
 fact=1
for j in range(1,i+1):
   fact=fact*j
ex=ex+(x**i)/(fact)
print(ex+1)
