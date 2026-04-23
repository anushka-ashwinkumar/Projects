while True:
#Title Printing
    print ("=====REPORT CARD MACHINE======")
    print ("Welcome")
    name = input ("Enter Student's Full Name: ")
    while True:
            grade = input("Enter Student's Grade (8/9/10): ")
            if grade == "8" or grade == "9" or grade == "10":
                break 
            else: 
                print ("Invalid Grade, Try Again")
    while True:
            section = input("Enter Student's Section (A/B/C): ").upper()
            if section == "A" or section == "B" or section == "C":
                break
            else: 
                print ("Invalid Section, Try Again")
    while True:
            math = int(input("Enter Student's Mathematics Marks: "))
            if math >= 0 and math <= 100:
                break
            else:
                print ("Invalid Math Marks, Try Again")
    while True:
            science = int(input("Enter Student's Science Marks: "))
            if science >= 0 and science <= 100:
                break
            else:
                print ("Invalid Science Marks, Try Again")
    while True:
            english = int(input("Enter Student's English Marks: "))
            if english >= 0 and english <= 100:
                break
            else:
                print ("Invalid English Marks, Try Again")
    total = math + science + english
    average = total/3
    if average >= 90:
            result = "A"
            comment = "Excellent"
    elif average >= 75:
        result = "B"
        comment = "Good"
    elif average >= 50:
        result = "C"
        comment = "Needs Improvement"
    else:
        result = "Fail"
        comment = "Needs to Work Hard"
    highest = max(math, science, english)
    
    print("========================")
    print("      REPORT CARD      ")
    print("========================")

    print("Name:", name)
    print("Grade:", grade)
    print("Section:", section)

    print("\n--- Marks ---")
    print("Math:", math)
    print("Science:", science)
    print("English:", english)

    print("\nTotal:", total)
    print("Average:", average)
    print("Highest Mark:", highest)
    print("Comment:", comment)

    print("\nResult:", result)
    again = input("Do you want to create another report card? (Yes/No): ").upper()
    if again != "YES":
            break
            
