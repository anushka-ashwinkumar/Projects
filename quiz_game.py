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

    ready = input("Are you ready for the Quiz? (yes/no): ").lower()

    if ready != "yes":
        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == "yes":
            print("Goodbye!")
            break
        else:
            continue

    try:
        file = open("questions.txt", "r")
        lines = file.readlines()
    except FileNotFoundError:
        print("questions.txt file not found! Please create the file first.")
        break

    if len(lines) == 0:
        print("No questions available!")
        file.close()
        break

    score = 0
    total_questions = 0

    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        parts = line.split("|")
        
        # Skip lines that don't have exactly a question and an answer
        if len(parts) != 2:
            print(f"Skipping improperly formatted line: {line}")
            continue
            
        total_questions = total_questions + 1

        question = parts[0].strip()
        answer = parts[1].strip()

        print("\n" + question)
        user_answer = input("Your answer (or type skip): ")

        if user_answer.lower() == "skip":
            print("Skipped ⏭️")
            continue

        if user_answer.strip().lower() == answer.lower():
            print("Correct 👍")
            score = score + 1
        else:
            print("Wrong ❌")
            print("Correct answer:", answer)

    file.close()

    print("\nFinal Score:", score)
    if total_questions > 0:
        percentage = (score / total_questions) * 100
        print("Percentage Correct:", percentage)

        if percentage >= 80:
            print("Excellent 🟢 Well done,", name + "!")
        elif percentage >= 50:
            print("Good 🟡 Keep improving,", name + "!")
        else:
            print("Try again 🔴 Don't give up,", name + "!")
    else:
        print("No valid questions were processed.")

    if not play_again():
        print("Goodbye!")
        break
    else:
        print("Restarting...\n")