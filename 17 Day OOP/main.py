from questions import Question
from data import question_data
from quiz_brain import QuizBrain

question_list=[]

for obj in question_data:
    text=obj["text"]
    answer=obj["answer"]
    
    question_list.append(Question(text,answer))
    
quiz=QuizBrain(question_list)

while quiz.still_has_question():
    
    quiz.NextQuestion()
    
