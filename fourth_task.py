students = [
    ("Иван", 20, 4.5),
    ("Мария", 19, 4.8),
    ("Пётр", 22, 4.2),
    ("Анна", 21, 4.7),
    ("Олег", 20, 3.9),
] # Список из кортежей

oldest = max(students, key=lambda student: student[1]) # Finding oldest student in list
best_student = max(students, key=lambda student: student[2]) # Finding sutdent with best grades
average_age = sum(student[1] for student in students) / len(students) # Finding average age of students

print("Students:")
for name, age, gpa in students:
    print(f"  {name:<6} age: {age:2}, GPA: {gpa}")
# Printing list of students

print(f"\nOldest student: {oldest[0]}, age {oldest[1]}")
print(f"Average age: {average_age:.2f}")
print(f"Best student: {best_student[0]} with {best_student[2]} points")

sorted_studs = sorted(students, key=lambda student: student[2], reverse=True)
print("\nBased on points:")
for name, age, gpa in sorted_studs:
    print(f"{name}: {age}")
# Printing sorted by grades list of students
