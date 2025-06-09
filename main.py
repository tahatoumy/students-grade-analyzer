
# Function to display students and their grades
def display_student_summary(names, grades):
    print("\n--- Students Summary ---")
    for i in range(len(names)):
        print(f"{names[i]}: {grades[i]}")

# Function to calculate average grade
def get_avg_grade(grades):
    return sum(grades) / len(grades)

# Function to get the highest grade and the student's name
def get_heighest_grade(names, grades):
    max_grade = max(grades)
    index = grades.index(max_grade)
    return names[index], max_grade

# Function to count students who passed (grade >= 60)
def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count


names = []
grades = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"Enter name of student #{i+1}: ")
    grade = float(input(f"Enter grade for {name} (out of 100): "))
    names.append(name)
    grades.append(grade)


display_student_summary(names, grades)

avg = get_avg_grade(grades)
print(f"\nAverage Grade: {avg:.2f}")

top_name, top_grade = get_heighest_grade(names, grades)
print(f"Highest Grade: {top_name} with {top_grade}")

passed_count = count_passed(grades)
print(f"Number of students who passed: {passed_count}")
