def welcome_message():
    print ("Welcome to Quiz Master Pro")
welcome_message()
def welcome_user():
    name = input("What is your name? : ")
    return name
user_name = welcome_user()
print("\n" + "Hello,", user_name.capitalize())
def run_quiz():
    score = 0
    quiz = {
        "What is the full name of Voldemort's mother?" : "Merope Gaunt",
        "What is the name of the goblin who accompanies Harry to his vault in Sorcerer's Stone?" : "Griphook",
        "Which Hogwarts house does Cedric Diggory belong to?" : "Hufflepuff",
        "What is the name of the magical prison guarded by Dementors?" : "Azkaban" }
    for question in quiz:
        print("\n" + question)

        user_answer = input("Your answer: ").strip().lower()
        correct_answer = quiz[question].strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! Correct answer is:", correct_answer)
    return score
score = run_quiz()
if score <= 1:
    print("\n" + "Better luck next time!")
elif score == 2: 
    print("\n" + "Good job!")
elif score >=3:
    print("\n" + "Excellent!")
print("You scored: " , score ," out of 4")
