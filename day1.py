"""
Project 1— "Student Grade Analyzer"

Problem Statement:
A school wants a CLI tool where a teacher can enter student names and their marks for 5 subjects. The tool should calculate grade, average, pass/fail, and display a summary report. No libraries — pure Python logic only.
Stack: Python (no external libraries)
Input: Student name + marks for 5 subjects (typed via terminal)
Output: Grade (A/B/C/F), Average score, Pass/Fail status, ranked list of students
Think about:
How do you store multiple students' data? (lists vs dictionaries)
What happens if someone enters text instead of a number?
How do you sort students by average without using sort() first?
Can you reuse logic using functions instead of repeating code?
"""

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")

    total = 0

    for j in range(5):
        m = float(input(f"Enter marks of subject {j+1}: "))
        total += m

    avg = total / 5

    # Grade
    if avg >= 75:
        grade = 'A'
    elif avg >= 60:
        grade = 'B'
    elif avg >= 50:
        grade = 'C'
    else:
        grade = 'F'

    # Pass/Fail
    if avg < 50:
        status = "Fail"
    else:
        status = "Pass"

    students.append([name, avg, grade, status])

#  SORTING
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] < students[j][1]:
            students[i], students[j] = students[j], students[i]

# OUTPUT
print("\n------ RESULT ------")

rank = 1
for s in students:
    print("\nRank:", rank)
    print("Name:", s[0])
    print("Average:", round(s[1], 2))
    print("Grade:", s[2])
    print("Status:", s[3])
    rank += 1
