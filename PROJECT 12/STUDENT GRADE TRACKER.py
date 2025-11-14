

def grade_tracker():
    print("=== Student Grade Tracker ===")
    name = input("Enter student name: ")
    try:
        num_subjects = int(input("Enter number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be more than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    grades = []
    for i in range(num_subjects):
        try:
            grade = float(input(f"Enter grade for subject {i+1}: "))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                return
            grades.append(grade)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return
    average = sum(grades) / num_subjects
    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print("\n=== Student Report ===")
    print(f"Name: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Result: {result}")
grade_tracker()
