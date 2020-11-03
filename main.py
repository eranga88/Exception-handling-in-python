from datetime import datetime,timedelta

class TicketMachine:

    def __init__(self,fare):
        self.fare = fare
        self.balance = 0

    def insertMoney(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def getPrice(self):
        return self.fare

    def getBalance(self):
        pass

    def printTicket(self):
        time = datetime.now().replace(second=0, microsecond=0) + timedelta(hours=5)
        print()
        print("################## TICKET###################")
        print("##                                        ##")
        print("##               VALID TILL               ##")
        print("##          "+str(time)+"           ##")
        print("##                                        ##")
        print("##               Thank You                ##")
        print("##                                        ##")
        print("############################################")
        print()

amount = 10
ticket = TicketMachine(amount)

selection = 1

print("Parking Fare is $",ticket.getPrice())

while not selection==0:
    print("Please select amount to Enter")
    print("1 - for $1 ")
    print("2 - for $2 ")
    print("3 - for 5$ ")
    print("4 - for 10$ ")
    print("5 - for 20$ ")
    print("6 - for 50$ ")
    print("7 - for $100 ")
    print(" 0 - to Exit ")

    try:
        selection = int(input("Enter your Selection : "))

        if selection <0:
            print("Please Enter Valid input")
            continue

    except ValueError:
        print("Please Enter Valid input")
        continue

    if not selection == 0:
        if selection in range(1,8):
            amount = 0
            if selection == 1:
                amount = 1
            if selection == 2:
                amount = 2
            if selection == 3:
                amount = 5
            if selection == 4:
                amount = 10
            if selection == 5:
                amount = 20
            if selection == 6:
                amount = 50
            if selection == 7:
                amount = 100
        else:
            print("Please Enter Valid input")
            continue

        if ticket.getPrice() > ticket.insertMoney(amount):
            print("Please Enter " + str(ticket.getPrice() - ticket.balance) + "$ to Print the Ticket")

        else:
            break

if selection == 0:
    print("User Cancelled the Transaction")
    if ticket.balance >0:
        print("Please Collect your Balance : ", ticket.balance)
        ticket.balance = 0


else:
    ticket.balance = ticket.balance - ticket.fare

    if ticket.balance > 0:
        print("Please Collect your Balance : ", ticket.balance)
    ticket.balance = 0

    ticket.printTicket()

    print("Your Balance is : ", ticket.balance)

