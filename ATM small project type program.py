username="nagaindra"
password="indra123"
c_name=input("enter your name:")
c_pass=str(input("enter your password:"))
if c_name==username and c_pass==password:
    print('''
    1.deposite
    2.withdraw
    3.mini_statement
    4.exit
    ''')
    amount=1000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("total amount:",amount)
    elif option==2:
        withd=int(input("enter the amount:"))
        amount-=withd
        print("ofter withdraw amount:",amount)
    elif option==3:
       print("=======ATM=======")
       print("username:",username)
       print("password:",password)
       print("total amount:",amount)
       print("thanks for visiting")
       print("===================")
    elif option==4:
       exit()
else:
    print("please enter correct login details")
       
          
    
  
            
  
  
           
