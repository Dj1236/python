hieght = input("tari hieght bol loda")
wieght = input("ketlo vajan che taro?")
bmi = int(wieght)/float(hieght)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

if bmi_as_int<18.5:
    print(f"your bmi is {bmi_as_int} you are under wieght")
elif bmi_as_int<25:
    print(f"your bmi is {bmi_as_int}you are normal wieght")
elif bmi_as_int<30:
    print(f"your bmi is {bmi_as_int}you  are obbese")
else :
    print("kuch toh gadbad hai daya")
            