credits = []
grades = []
for _ in range(20):
    _, credit, grade = input().split()
    if grade != "P":
        credits.append(float(credit))
        grades.append(grade)

table = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

total = 0
for i, grade in enumerate(grades):
    total += credits[i] * table[grade]

average = total / sum(credits)
print(average)