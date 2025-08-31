password=int(input("Enter The Password ->"))
if password==2025:
    print("___WELCOME TO THE LOAN CALCULATOR___")
    amount=int(input("Enter The Principal Amount ->"))
    interest=int(input("Enter The Rate Of Interest ->"))
    time=int(input("Enter Number Of Years ->"))
    i=amount*interest*time/100
    payments=time*12
    famount=i+amount
    print("Total Interest ->",i)
    print("Total Number Of Payments ->",payments)
    print("Total Amount To be Paid ->",famount)

    print("________________________________________")
    print("DAY WISE PAYMENTS")
    print("Day----Amount")
    for a in range(1,time+1):
        print(a,amount+i)
        a+=1
        print("___________________________________ ")

else:
    print("You Entered An Invalid Keyy")
    print("1.Forgot Password")
    print("2.Exit")
    h=int(input("Choose Your Recovery Option Or Exit->"))
    if h==1:
        print("RECOVERY MODE")
        newkey=int(input("Enter The New Password->"))
        key=int(input("Confirm The New Password->"))
        if newkey==key:
            password=key
        else:
            print("Wrong Attempt")
    else:
        print("Thank You Visit Again ")
        
    

































    
    
