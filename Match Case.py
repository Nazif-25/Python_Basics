grade = input("Enter your grade: ").upper()

match grade:
    case "A":
        print("Exceptional")
    case "B":
        print("Good")
    case "C":
        print("Can do better")