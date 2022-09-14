a={1:20,'aaa':30,3:40,'bbb':50}
b=len(a)
print(b)
#we are creating list to convert dict:
c=[(1,20),(2,30),(3,50),(4,56)]
d=dict(c)
print(d)
#we can create key()
e={'naga':10,'bujji':20,'mam':30}
f=e.keys()
print(f)

#we can create a values():
g={'naga':10,'bujji':20,'mam':30}
h=g.values()
print(h)
#we can create a item():
s={'naga':10,'bujji':20,'mam':30}
r=s.items()
print(r)
#we can create a get():
n={'naga':10,'bujji':20,'mam':30}
m=n.get('naga')
print(m)
#update():
v={'naga':10,'bujji':20,'mam':30}
v1={'jyo':50,'ba':50}
u=v.update(v1)
print(v)
#delet():
z={'naga':10,'bujji':20,'mam':30}
del z['naga']
print(z)
#clear():
x={'naga':10,'bujji':20,'mam':30}
x.clear()
print(x)

