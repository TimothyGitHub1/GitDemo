# import necessary modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# show question

# print(question_data[0])
# print(question_data[0]["text"])
# print(question_data[0]["answer"])
# new_q2 = Question("2+3=5", "True")
#new_q3 = Question(question_data[0]["text"], question_data[0]["answer"])

#print(new_q3.text, new_q3.answer)

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# This is a new comment for git

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")




# for x in question_bank:
#     print(question_bank[x].text +" - "+ question_bank[x].answer)
