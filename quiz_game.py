print("=================================")
print("       QUIZ MASTER PRO 🎮       ")
print("=================================")
print("Answer carefully!")
print("Type skip to skip a question")
print()

name = input("Enter your name: ")
print("\nWelcome,", name + " 🎮")

def play_again():
    answer = input("\nDo you want to play again? (yes/no): ")
    return answer.strip().lower() == "yes"


while True:

    ready = input("Are you ready for the Harry Potter Quiz? (yes/no): ").lower()

    if ready != "yes":
        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == "yes":
            print("Goodbye!")
            break
        else:
            continue

    file = open("questions.txt", "r")

    lines = file.readlines()

    if len(lines) == 0:
        print("No questions available!")
        file.close()
        break

    score = 0
    total_questions = 0

    for line in lines:
        total_questions = total_questions + 1

        line = line.strip()
        parts = line.split("|")

        question = parts[0]
        answer = parts[1]

        print("\n" + question)
        user_answer = input("Your answer (or type skip): ")

        if user_answer.lower() == "skip":
            print("Skipped ⏭️")
            continue

        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct 👍")
            score = score + 1
        else:
            print("Wrong ❌")
            print("Correct answer:", answer)

    file.close()

    print("\nFinal Score:", score)
    percentage = (score / total_questions) * 100
    print("Percentage Correct:", percentage)

    if percentage >= 80:
        print("Excellent 🟢 Well done,", name + "!")
    elif percentage >= 50:
        print("Good 🟡 Keep improving,", name + "!")
    else:
        print("Try again 🔴 Don't give up,", name + "!")

    if not play_again():
        print("Goodbye!")
        break
    else:
        print("Restarting...\n")