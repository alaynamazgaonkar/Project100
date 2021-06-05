class atm:
    def __init__(self,cardNumber,pinNumber,balance):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.balance=balance
    
    def cashWithdrawal(self,balance):
        cash=int(input("Enter the amount you wish to withdraw :- "))
        balance=balance-cash
        print(balance)

    def balanceEnquiry(self,balance):
        print("Balance :- "+balance)

card=input("Enter your card number :- ")
pin=input("Enter your pin number :- ")
print("")
acc= atm(card,pin,100)
end="false"

print("Enter c for cash withdrawal, b for balance enqiury")
func=input("or e to exit :- ")
if func=="c":
    acc.cashWithdrawal(acc.balance) 
elif func=="b":
    acc.balanceEnquiry(acc.balance)
elif func=="e":
    print("")
    print("atm has ended.")
    end="true"
print("")

if end=="false":
    print("Enter c for cash withdrawal, b for balance enqiury")
    func=input("or e to exit :- ")
    if func=="c":
        acc.cashWithdrawal(acc.cardNumber)
        print("")
        print("atm has ended.")
    elif func=="b":
        acc.balanceEnquiry(acc.balance)
        print("")
        print("atm has ended.")
    elif func=="e":
       print("atm has ended.")
    print("")