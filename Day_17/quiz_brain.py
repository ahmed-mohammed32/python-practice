# QuizBrain class
import sys


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there is still a question in the question bank
           Returns False if no question left"""
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        if self.question_number < len(self.question_list):
            c_question = self.question_list[self.question_number]
            # Go to the next question number
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {c_question.text} (True/False)?: ")
            self.check_answer(user_answer, c_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

