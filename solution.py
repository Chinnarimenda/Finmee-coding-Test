def student_with_highest_average(students):
    highest_avg = 0
    top_student = None

    for student in students:
        grades= student["grades"]
        avg= sum(grades)/ len(grades)

        if avg>highest_avg:
            highest_avg= avg
            top_student = student
    return top_student

students=[
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [76, 82, 80]}
]
result = student_with_highest_average(students)
if result:
    avg = sum(result['grades']) / len(result['grades'])
    print(f"{result['name']}: {avg:.2f}")
else:
    print("No students found")