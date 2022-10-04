class library():
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print("available")
        for book in self.books:
            print(book)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("get your book")
            self.books.remove(borrow_book)
        else:
            print("book is not available")
    def receive_book(self,receive_book):
        print("you have return the book")
        self.books.append(receive_book)
books=['python','c','java','html','css','javascript']
a=library(books)
msg='''
1.display book
2.borrow book
3.return book
'''
while True:
    print(msg)
    b=int(input("enter your choice:"))
    if b==1:
        a.list_books()
    elif b==2:    
        book=input("enter book name:")
        a.borrow_book(book)
    elif b==3:
        book=input("enter the book name return the book:")
        a.receive_book(book)
    else:
        print("thank you come again:")
        quit()
