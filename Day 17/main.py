# Step 1: Import the 'blueprint' (Question class) and the raw source data (list of dictionaries)
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialize an empty container to store our "smart" objects
question_bank = []

# Iterate through the raw list of dictionaries to extract data
for question in question_data:
    question_text = question["text"]            # Access values from the current dictionary using their specific keys
    question_answer = question["answer"]

    # --- OOP INSTANTIATION ---
    # Create a NEW instance of the Question class.
    new_question = Question(q_text=question_text, q_answer=question_answer) # We pass the raw strings as arguments
                                                                            # to initialize the object's attributes.
    question_bank.append(new_question) # Store the fully-formed object into our question_bank list

# Printing the bank will display the object references (memory addresses)
# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print()
print("You've complete the quiz")
print(f"Your final score was: {quiz.score} / {len(question_bank)}")
