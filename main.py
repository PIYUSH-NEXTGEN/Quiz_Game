from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


name = input("Enter your name: ")
print(f"Welcome, {name}! Let's start the quiz 🎯")
def run_quiz():


    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    random.shuffle(question_bank)
    selected_questions = question_bank[:10]  # Pick only 10 random questions
    quiz = QuizBrain(selected_questions)

    quiz1 = QuizBrain(question_bank)

    wrong_attempts = 0
    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz")
    print(f"Your score was: {quiz.score}/{quiz.question_number}")


while True:
    run_quiz()
    play_again = input("🔁 Want to play again? (yes/no): ").lower()
    print("\n" )
    if play_again != "yes":
        print(f"👋 Thanks for playing '{name}' ! See you next time.")
        break











