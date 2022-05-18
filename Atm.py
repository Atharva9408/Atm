class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your Balance is 50000")

    def withdrawal(self, amount):
        new_amount = 50000-amount
        print("You have Withdrawn amount "+str(amount) + ". Your reamaining balance is "+str(new_amount))

def main():
    Card_Number = input("Insert your card number: ")
    pin_number = input("Enter your pin number: ")

    new_user = Atm(Card_Number, pin_number)

    print("Choose your activity")
    print("1.Balance Enquiry, 2.Withdrawal")
    activity = int(input("Enter activity number: "))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount= int(input("Enter the amount:"))
        new_user.withdrawal(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()