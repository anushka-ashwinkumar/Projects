while True:
    options = input("Type '1' to add, '2' to view, '3' to delete, '4' to exit: ")

    if options == "1":
        print("Ok, sure!")

        while True:
            file = open("questions.txt", "a")

            question = input("Enter a question: ")
            answer = input("Enter the answer: ")

            file.write(question.strip() + "|" + answer.strip() + "\n")
            file.close()

            more = input("Add another question? (yes/no): ")

            if more.lower() != "yes":
                break

    elif options == "2":
        file = open("questions.txt", "r")

        count = 1

        for line in file:
            parts = line.strip().split("|")
            print(str(count) + ".", parts[0])
            print("Answer:", parts[1])
            print()
            count = count + 1

        print("Total Questions:", count - 1)

        file.close()

    elif options == "3":
        file = open("questions.txt", "r")
        lines = file.readlines()
        file.close()

        count = 1
        for line in lines:
            parts = line.strip().split("|")
            print(str(count) + ".", parts[0])
            count = count + 1

        delete_num = int(input("Enter question number to delete: "))
        index = delete_num - 1

        if index >= 0 and index < len(lines):
            confirm = input ("Are you sure you want to delete thsi question?: (Yes/No):")
            if confirm.lower() == "yes":

                lines.pop(index)

                file = open("questions.txt", "w")

                for line in lines:
                    file.write(line)

                file.close()

                print("Question deleted successfully 👍")
            else: 
                print("Delete cancelled ❌")

        else:
            print("Invalid question number ❌")

    elif options == "4":
        print("Goodbye!")
        break

    else:
        print("Sorry! Choose a valid option.")
