print("welcome to rollercosater")
hieght =input("what is your hieght")

if hieght>=120:
    print("you can ride")
    age=int(input("umar ketli che tari"))
    if age<12:
        bill =50
        print("50 rupia thai che")
    elif age<= 18:
        bill=18
        print("70 rupia thai che")
    elif age<=1000:
        bill =1236
        print("tu haji ka jive cho")    
    else:
        bill =120
        print("120 rupia thai che") 
    photo_joei=input("joie che ke nai photo")
    if photo_joei =="Y":
        bill+=3
        


else:
    print("nai besva male thatu hoi e kari le")
 
