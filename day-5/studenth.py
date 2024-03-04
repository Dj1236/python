students_hieght=input("list of student hieght").split()
for n in range(0,len(students_hieght)):
    students_hieght[n]=int(students_hieght[n])
print(students_hieght)    

total_hieght=0
for hieght in total_hieght:
    total_hieght+=hieght
    print(total_hieght)


number_of_students=0
for student in students_hieght:
    number_of_students += 1
print(number_of_students)    


average_hieght= round(total_hieght/number_of_students)
print(average_hieght)

