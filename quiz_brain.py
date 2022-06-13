import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_no]
        self.question_no += 1
        q_text = html.unescape(self.current_question.question)
        return (f"Q.{self.question_no}:{q_text}")
        # user_answer = input(f"Q.{self.question_no}:{q_text}: (True/False):  ")
        # self.check_answer(user_answer, self.current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
