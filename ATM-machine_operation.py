
#ATM Machine
print("--------------------Welcome to our ATM Machine-----------------")
pin=9999
i=0
while i<3:
    u_pin=int(input("Enter your 4 digit pin:"))

    if u_pin==pin:
        print("Login Successfully")

        print("-----ATM Operations-----")
        print("1. Balance Enquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Exit")

        while True:

            choice =int(input("Enter your choice (1-4):"))
            balance=10000

            if choice==1:
                print("Your current balance is:",balance)
            elif choice==2:
                withdraw=int(input("Enter your Withdraw amount:"))
                if withdraw <=balance:
                    balance-=withdraw
                    print("Please collect your cash")
                    print("After Withdraw Your updated balance is:",balance)
                else:
                    print("Insufficient Balance..!!")
            elif choice==3:
                dep=int(input("Enter your Deposit amount:"))
                balance+=dep
                print("Your Amount has been Deposited Successfully")
                print("After Deposit Your updated balance is:",balance)
            elif choice == 4:
                print("Thank you for using our ATM")
                break        
            else:
                print("Invalid choice, Please try again")
        break
    else:
        print("Invalid Pin, Please try again")
    i+=1
else:
    print("Your account is blocked")