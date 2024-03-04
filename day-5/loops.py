from functools import total_ordering


fruits =["keri","tarbuch","draksh","keda"]
for fruit in fruits:
    print(fruit)
    print(fruit + "ras")
print(fruits) 

for number in range(1,10,3):
    print(number)
for number in range(1,101):
    total_ordering+=number
    print(total_ordering)

for number in range(2,101,2):
    total_ordering+=number
    print(number)

for number in range(1,101):
    if number%2 ==0:
        total_ordering+=number
        print(total_ordering)
        
