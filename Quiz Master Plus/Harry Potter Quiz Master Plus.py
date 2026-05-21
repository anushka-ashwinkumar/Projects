questions = ["What is the name of the Apparition instructor who visits Hogwarts in Harry's sixth year?", "Which row in the Hall of Prophecy contains the prophecy about Harry Potter and Lord Voldemort?","In 'The Goblet of Fire', what are the three ingredients required to restore Lord Voldemort to his body?", "What is the full name of the Gray Lady, the Ravenclaw House ghost?", "What is the only book in the Harry Potter series where the title character does not appear in the very first chapter?"]
answers = ["Wilkie Twycross", "Row 97", "bone of the father, flesh of the servant, blood of the enemy", "Helena Ravenclaw", "Harry Potter and the Goblet of Fire"]
print("__________________Harry Potter Quiz Master Plus__________________")
print("Welcome!")
name = input("What is your name:")
while True:
    ready = input("Are you ready for the Harry Potter Quiz? (Yes/No):").upper()
    if ready == "YES":
        print("Great, let's get started")
        break
    elif ready == "NO":
        exit_choice = input("Do you want to exit? (Yes/No): ").upper()

        if exit_choice == "YES":
            print("Okay, goodbye!")
            exit()
        else:
            print("No problem, take your time")
while True:
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i])
        if user_answer.lower() == answers[i].lower():
                score = score + 1
                print("Correct!")
        else:
                print("Wrong!")
                print("The correct answer is", answers[i])
    print("Quiz finished!")
    print("Your score is:", score, "/", len(questions))
    if score == len(questions):
        print("Excellent!")
    elif score >= 3:
        print("Good job")
    elif score >= 1:
        print("Not bad, keep practicing")
    else:
        print("Better luck next time")
    again = input("Would you like to play again? (Yes/No):").upper()
    if again == "YES":
        print("Ok, let the magic continue")
        continue
    else:
        print("Thanks for playing!")
        break# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
