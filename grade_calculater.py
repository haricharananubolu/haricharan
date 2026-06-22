# NAME=Hari charan
# Creating a grade_calculator

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def grade_comments(grade):
    if grade == 'A':
        return "Excellent work!"
    elif grade == 'B':
        return "Good job!"
    elif grade == 'C':
        return "You can do better."
    elif grade == 'D':
        return "Needs improvement."
    else:
        return "Failing grade. Please seek help."


num_students = 0

while num_students <= 0:
    num_students = int(input("Enter the number of students: "))

    if num_students <= 0:
        print("Enter positive numbers only")

names = []
marks = []

# Step 4: Collect Data
for i in range(num_students):

    name = input("Enter your name: ")

    while True:
        m1 = int(input("Enter the marks of subject 1: "))
        if 0 <= m1 <= 100:
            break
        else:
            print("Enter only marks between 0 and 100")

    while True:
        m2 = int(input("Enter the marks of subject 2: "))
        if 0 <= m2 <= 100:
            break

    while True:
        m3 = int(input("Enter the marks of subject 3: "))
        if 0 <= m3 <= 100:
            break

    names.append(name)
    marks.append([m1, m2, m3])

# Step 5: Calculate Results
result = []
class_total = 0

for i in range(num_students):

    average = sum(marks[i]) / 3
    grade = calculate_grade(average)
    comment = grade_comments(grade)

    result.append([names[i], average, grade, comment])
    class_total += average

# Calculate class statistics
class_average = class_total / num_students

highest_average = result[0][1]
lowest_average = result[0][1]

for student in result:
    if student[1] > highest_average:
        highest_average = student[1]

    if student[1] < lowest_average:
        lowest_average = student[1]


# Step 6: Display Results
print("\n" + "=" * 70)
print("                     STUDENT REPORT")
print("=" * 70)

print(f"{'Name':<15}{'Average':<15}{'Grade':<10}{'Comment'}")
print("-" * 70)

for student in result:

    name = student[0]
    average = student[1]
    grade = student[2]
    comment = student[3]

    # Color coding
    if grade == 'A':
        color = "\033[92m"    # Green
    elif grade == 'B':
        color = "\033[94m"    # Blue
    elif grade == 'C':
        color = "\033[93m"    # Yellow
    else:
        color = "\033[91m"    # Red

    reset = "\033[0m"

    print(color + f"{name:<15}{average:<15.2f}{grade:<10}{comment}" + reset)

print("-" * 70)

print(f"Class Average : {class_average:.2f}")
print(f"Highest Average : {highest_average:.2f}")
print(f"Lowest Average : {lowest_average:.2f}")


# Step 7: Search for a specific student
search_name = input("\nEnter student name to search: ")

found = False

for student in result:

    if student[0].lower() == search_name.lower():

        print("\nStudent Found")
        print("Name :", student[0])
        print("Average :", round(student[1], 2))
        print("Grade :", student[2])
        print("Comment :", student[3])

        found = True
        break

if found == False:
    print("Student not found")


# Save results to a file
file = open("student_results.txt", "w")

file.write("STUDENT REPORT\n")
file.write("=" * 70 + "\n")

for student in result:
    file.write(
        f"Name: {student[0]} Average: {student[1]:.2f} Grade: {student[2]} Comment: {student[3]}\n"
    )

file.write("\n")
file.write(f"Class Average: {class_average:.2f}\n")
file.write(f"Highest Average: {highest_average:.2f}\n")
file.write(f"Lowest Average: {lowest_average:.2f}\n")

file.close()

print("\nResults saved successfully in student_results.txt")    

    
    