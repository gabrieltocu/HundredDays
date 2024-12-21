student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for score in student_scores.values():
    if 91 <= score <= 100:
        student_grades[score] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[score] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[score] = "Acceptable"
    elif score <= 70:
        student_grades[score] = "Fail"

# Make each key of the student_grades dictionary the same keys as student_scores dictionaries
for key in student_scores.keys():
    student_grades[key] = student_grades[student_scores[key]]
    del student_grades[student_scores[key]]

print(student_grades)