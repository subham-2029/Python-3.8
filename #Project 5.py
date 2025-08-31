#speed converter
print("WELCOME TO SPEED CONVERTER")
print("1. Kilometer to meter per second")
print("2. meter to kilomeeter per second")
h=int(input("Enter Your Choice 1 or 2 ->"))
if h ==1:
    print("kilometer to meter")
    km=int(input("Enter speed->"))
    m=km*5/18
    print("the speed is ",m,"/sec")
    print("Completed")
