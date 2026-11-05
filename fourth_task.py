students = [
    ("Иван", 20, 4.5),
    ("Мария", 19, 4.8),
    ("Пётр", 22, 4.2),
    ("Анна", 21, 4.7),
    ("Олег", 20, 3.9),
]

oldest = max(students, key=lambda student: student[1])
best_student = max(students, key=lambda student: student[2])
average_age = sum(student[1] for student in students) / len(students)

print("Students:")
for name, age, gpa in students:
        print(f"  {name:<6} age: {age:2}, GPA: {gpa}")

print(f"\nOldest student: {oldest[0]}, age {oldest[1]}")
print(f"Average age: {average_age:.2f}")
print(f"Best student: {best_student[0]} with {best_student[2]} points")

sorted_studs = sorted(students, key=lambda student: student[2], reverse=True)
print("\nBased on points:")
for name, age, gpa in sorted_studs:
    print(f"{name}: {age}")
