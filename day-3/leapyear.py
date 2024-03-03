year=int(input("kayo varas jovo che tare"))
if year% 4==0:
    if year%100==0:
        if year%400==0:
            print("che ho bhai leap varas")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not leap year")                


