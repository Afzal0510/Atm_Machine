class BankAccount:
    def __init__(self) :
        self.amount=0
    def deposit(self,Amount):
            self.amount+=Amount
            print(" Amount Successfully deposit ")

    def withdrawn(self,Amount):
            if(self.amount-Amount>=500) :
                self.amount-=Amount
                print(" Amount Successfully withdrawn ")   
            else :
                print("Insufficient balance :  You have to keep atleast 500 ")
    def display(self):
            print(" Your Bank balance is : " , self.amount)

atm=BankAccount()
for i in range(10):
    print(" 1 .Depost 2.withdrawn 3.display 4.Exit")
    try:
        p=int(input("Enter your choice :"))
    
        if(p==1):
            Amount=float(input("Enter amount to be deposit : "))
            atm.deposit(Amount)
        elif(p==2):
            Amount=float(input("Enter amount to be withdrawn : "))
            atm.withdrawn(Amount)
        elif(p==3) :
            atm.display()
        elif(p==4):
            exit()
      #  else :
            
    except :
        print(" You have enter wrong number : ")
        


        



                





        