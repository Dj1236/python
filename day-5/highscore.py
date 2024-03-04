student_scores=input("ketla aaiva?").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)    
#print(max(student_scores))
hieghest_score=0
for score in student_scores:
    if score>hieghest_score:
        hieghest_score=score
        print('The highest score is',str(hieghest_score),'.')
         

