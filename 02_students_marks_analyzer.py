"""
Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def add_students():
    students = {}
    
    while True:
        name = input("\nEnter the name of student or 'exit' to end : ").strip().lower()
        if name.lower() == "exit":
            break
        if name in students:
            print("student already exists !!")
            continue
        try:
            score = float(input(f"Enter score of {name} : "))
            students[name] = score 
        except ValueError:
            print("Enter valid marks !!")

    return students

def student_result(students):
    if not students:
        print("No student data found !!")
        return 
    
    marks = list(students.values())

    max_score = max(marks)
    min_score = min(marks)
    avg_score = sum(marks)/len(students)

    topper = [name for name,score in students.items() if score == max_score]
    bottomer = [name for name,score in students.items() if score == min_score]

    print(f"\n{'-'*20}Students Marks Analysis{'-'*20}")
    print(f"Total students : {len(students)}")
    print(f"Average marks for students : {avg_score:.2f}")
    print(f"Maximum score {max_score} scored by {','.join(topper)}")
    print(f"Minimum score {min_score} scored by {','.join(bottomer)}\n")

    print(f"\n{'-'*24}Detailed Marks{'-'*25}")
    for name, marks in students.items():
        print(f"- {name} : {marks}")

students = add_students()
student_result(students)
