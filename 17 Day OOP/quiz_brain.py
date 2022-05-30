class QuizBrain:
    
    def __init__(self,q_list):
        self.question_number=0
        self.q_list=q_list
        self.counter=0
    
    def still_has_question(self):
        return len(self.q_list)>self.question_number        
        
        
    def NextQuestion(self):
        
        current_question=self.q_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number} {current_question.text}")
        user_answer=input("Answer t/f?  ")
        self.check_answer(user_answer,current_question.answer)
        
    def check_answer(self,userAnswer,corrAnswer):
        if userAnswer.lower()==corrAnswer.lower():
            print("That was a correct answer")
            self.counter+=1
        else:
            print("That was not a correct answer")
        
        print(f"Your score is {self.counter}/{self.question_number}")
    
    