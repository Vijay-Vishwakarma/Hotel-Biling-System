class hotel:
    print ("          WELCOME TO KAiLASH DA DHABA     ")
    print()


    def __init__(self,gt=0,tt=0,v=0,n=0):
        self.gt=gt
        self.tt=tt
        self.n=n
        self.v=v


    def veg(self):

        print("     VEG MENU     ")

        print("1.Masala Dosa-----Rs40","2.Vadapav-----Rs15","3.Samosa-----Rs18","4.Veg Thali-----Rs150","5.Chai-----Rs10","6.Exit")
        c=int(input("Enter your choice: "))
        if (c==1):
            d=int(input("Enter the quantity: "))
            self.v=self.v+40*d

        elif (c==2):
            d=int(input("Enter the quantity: "))
            self.v=self.v+15*d

        elif (c==3):
            d=int(input("Enter the quantity: "))
            self.v=self.v+18*d

        elif (c==4):
            d=int(input("Enter the quantity: "))
            self.v=self.v+150*d

        elif (c==5):
            d=int(input("Enter the quantity: "))
            self.v=self.v+10*d

        else:
            print("Not Available")
       
    def nonveg(self):
        print("     NON-VEG MENU     ")
        print("1.Thandori Chicken-----Rs240","2.Chiken Rice-----Rs100","3.Egg Kari-----Rs80","4.NONVEG Thali-----Rs200","6.Exit")
        c=int(input("Enter your choice: "))

        if (c==1):
            d=int(input("Enter the quantity: "))
            self.n=self.n+40*d

        elif (c==2):
            d=int(input("Enter the quantity: "))
            self.n=self.n+15*d

        elif (c==3):
            d=int(input("Enter the quantity: "))
            self.n=self.n+15*d

        elif (c==4):
            d=int(input("Enter the quantity: "))
            self.n=self.n+150*d
     
        else:
            print("Not Available")

       
    def display(self):
        self.gt=self.v+self.n
        print("Your Cost for ordered food is",self.gt,"Rs")
        self.tt=self.gt+(self.gt)*(5/100)
        print("Your total Bill is :",self.gt,"Rs","+","GST:- 5%","=",int(self.tt),"Rs")
              

h=hotel()
opt='y'
while(opt is 'y' ):
    ch=int(input("Enter your Choice: 1.Veg 2.NonVeg :- "))
    if(ch==1):
        h.veg()
    elif(ch==2):
        h.nonveg()
    else:
        print("invalid option")
    opt=input(("Sir/Madam Do you want order again(y/n)? "))
h.display()
print("Thanks For Coming to KAiLASH DA DHABA")
