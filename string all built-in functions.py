#string functions:
a='nagajyothi'
print(len(a))
print(max(a))
print(min(a))
print(sorted(a))
## Writing a built in functions and methods:
b='jyothi nagaraju'
print(b.title())
print(b.lower())
print(b.upper())
c='hi hi how are you all hi friends'
d=c.count('hi')
print(d)
d=c.count('hi',0,8)
print(d)
d=c.count('hi',8,25)
print(d)
print(c.find('how'))
print(c.find("friends"))
#index built-in function
s='abc def ghi jkl mno pqr stu vwx yz!'
print(s.index('ef'))
print(s.index('yz'))
print(s.index('!'))
'''we con't write a string that string we can write in a print statement the print stament is erorr comes:
print(s.index('hee'))'''
#Writing a builting function "endswith" or "startswith"
n="python string!"
print(n.endswith("!"))
print(n.endswith('string'))
print(n.startswith('python'))
#String functins "is" functions
b="iloveyou"
print(b.isalnum())
print(b.isalpha())
print(b.isdigit())
print(b.islower())
print(b.isupper())
print(b.isspace())
print(b.istitle())
