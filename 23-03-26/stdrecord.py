students = {}

def add_student(name, marks):
    students[name] = marks

def average(name):
    return sum(students[name]) / len(students[name])

def topper():
    return max(students, key=lambda x: average(x))

add_student("Anshu", [80, 90])
add_student("Ravi", [70, 60])

print("Topper:", topper())