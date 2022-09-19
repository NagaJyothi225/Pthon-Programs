class car:
    def __init__(self,carmanufactulae,carmanufactularyear,carvarient):
        self.a=carmanufactulae
        self.b=carmanufactularyear
        self.c=carvarient
    def car1(self):
        print(self.a,self.b,self.c)
x=car('tata',2022,'diesel')
x.car1()

