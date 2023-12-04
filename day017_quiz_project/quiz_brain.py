class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.score = 0
        self.question_number = 0

    def still_has_questions(self, q_list):
        while len(q_list) > 0:
            return True

    def next_question(self):
        self.question_number += 1
        question = self.q_list.pop()
        user_answer = input(f"{self.question_number}. {question.question} True or False? ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
