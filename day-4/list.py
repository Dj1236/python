import random
#states_of_Bharat =["gujrat","raistan","madhyapradesh","maharastra","uttarpradesh","andhrapradesh",  ]
#print(states_of_Bharat[0])
names_string = input("enter your names")
names = names_string.split(",")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_will_pay =names[random_choice]
print(f"{person_who_will_pay} + aa pikinno bil dehe")


