def welcome_message():
    print ("Welcome to Quiz Master Pro")
def welcome_user():
    name = input("What is your name? : ")
    return name
def run_quiz():
    score = 0
    question_number = 1
    quiz = {
        "What is the full name of Voldemort's mother?" : "Merope Gaunt",
        "What is the name of the goblin who accompanies Harry to his vault in Sorcerer's Stone?" : "Griphook",
        "Which Hogwarts house does Cedric Diggory belong to?" : "Hufflepuff",
        "What is the name of the magical prison guarded by Dementors?" : "Azkaban" }
    for question in quiz:
        print(f"\nQ{question_number}: {question}")
        question_number += 1

        user_answer = input("Your answer: ").strip().lower()
        correct_answer = quiz[question]

        if user_answer == correct_answer.lower():
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! Correct answer is:", correct_answer)
    return score
def show_result(score):
    if score <= 1:
        print("\n" + "Better luck next time!")
    elif score == 2: 
        print("\n" + "Good job!")
    elif score >=3:
        print("\n" + "Excellent!")
    print("You scored: " , score ," out of 4")
welcome_message()
user_name = welcome_user()
print("\nHello,", user_name.capitalize())
def play_again():
    answer = input("Do you want to play again? (yes/no): ").strip().lower()
    if answer == "yes":
        return True
    else:
        return False
while True:
    score = run_quiz()
    show_result(score)
    
    if not play_again():
        break
