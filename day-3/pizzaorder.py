print("pizza khava haila aavo ")
size = input("ketlo moto levo che modha ma ")
add_peproni=input("peproni nakhi che ")
extra_cheese=input("jado thai jai extra cheese thi")
bill =0
if size =="s":
    bill +=15
elif size =="m":
     bill+=20
else:
     bill+=25

if add_peproni=="y":
     if size == "s":
          bill += 2
     else :
          bill +=3

if extra_cheese =="Y":
     bill +=4
           
print(f"haal {bill}etla paisa de")
      
