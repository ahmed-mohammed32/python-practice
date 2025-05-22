from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# New empty list for question bank
question_bank = []

# Adding the question_data dictionary to the question bank
for question in question_data:
    question_text   = question["question"]
    question_answer = question["correct_answer"]
    new_question =  Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # If quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
