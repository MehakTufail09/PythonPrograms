'''Online Quiz Application: Develop an online quiz application with classes like Quiz, Question, and Participant.
Use inheritance to represent different types of quizzes (e.g., multiple-choice, true/false).'''


class Questions:
    def __init__(self, text, options, correctOption):  # this is the constructer
        self.text = text
        self.options = options
        self.correctOption = correctOption

    def isCorrect(self, userAnswer):  # the function returning the value of user answer which is correct option
        return userAnswer == self.correctOption


class Quiz:
    def __init__(self, name, questions):  # this is constructer
        self.name = name
        self.questions = questions

    # function for conducting the quiz
    def conductQuiz(self, user):
        print(f"Welcome to the {self.name} Quiz!\n")
        userScore = 0
        # Loop through the questions using a range and an index counter
        for i in range(len(self.questions)):
            question = self.questions[i]
            print(f"Question {i + 1}: {question.text}")
            # Display the options for the question
            for option in question.options:
                print(f"  {option}")

            # Get the participant's answer
            userAnswer = input("Your answer: ")
            # Check if the answer is correct
            if question.isCorrect(userAnswer):
                print("Correct!\n")
                userScore += 1
            else:
                print(f"Wrong! The correct answer is {question.correctOption}\n")

        # Display the participant's final score
        print(f"Quiz completed! Your score: {userScore}/{len(self.questions)}\n")


# the class inheriting the question class
class MultipleChoiceQuestion(Questions):
    def __init__(self, text, options, correctOption):
        super().__init__(text, options, correctOption)


# the class inheriting the question class
class TrueFalseQuestion(Questions):
    def __init__(self, text, correctOption):
        options = ["True", "False"]
        super().__init__(text, options, correctOption)


class Participant:

    def __init__(self, name):  # constructer
        self.name = name


question1 = MultipleChoiceQuestion("What is the capital of France?", ["A. Paris", "B. Berlin", "C. Madrid"], "A")
question2 = TrueFalseQuestion("The Earth revolves around the Sun.", "True")
question3 = MultipleChoiceQuestion("Which programming language is this quiz written in?",
                                   ["A. Python", "B. Java", "C. C++"], "A")

quiz = Quiz("Programming Quiz", [question1, question2, question3])

participant1 = Participant("Mehak")
quiz.conductQuiz(participant1)