class quizBrain:
    def __init__(self,q_list):
        self. question_number = 0
        self. score =0
        self.question_list = q_list

    def still_have_question(self) :
        return self.question_number < len(self.question_list):
     

    def next_question(self):
        current_question =self.question_list[self.question_number]
        self.question_number += 1
        input(f"q.{self.question_number} : {current_question.text} (true/false)")
        self.check_answer (user_answer,current_question.answer)

    def check_answer(self,user_answer,current):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you fot it right")
        else:
            print("you got it wrong")    
            print(f"this is cureent answer{correct_answer}")
