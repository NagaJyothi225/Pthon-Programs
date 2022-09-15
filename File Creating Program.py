my_file=open("C:/Users/nagaj/OneDrive/Desktop/New Text Document.txt",'r')
my_file=open("C:/Users/nagaj/OneDrive/Desktop/New Text Document.txt",'w')

my_file.write("hi my self nagajyothi \nwe are learning python\ni am evary good girls")
item=["\nthis is my first line","\nthis is my second line","\nthis is my thrid line"]
my_file.writelines(item)
item1=["\n i am interested"]
my_file.writelines(item1)
my_file.write("\nhello all off you")
my_file=open("C:/Users/nagaj/OneDrive/Desktop/New Text Document.txt",'r+')
#my_file.read(10)
#print(my_file.read(10))
#my_file.readline(5)
#my_file.tell()
#print(my_file.seek(2))
#my_file.write("hihihi")
#print(my_file.readline(15))
my_file=open("C:/Users/nagaj/OneDrive/Desktop/New Text Document.txt",'a')
print(my_file.write('\nbujji'))

my_file.close()
