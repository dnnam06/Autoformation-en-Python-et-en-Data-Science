from functions_students import biggest_integer, smallest_integer, print_students

students = [
    {"id": "SV001", "name": "Nguyễn Văn An", "age": 20, "gpa": 16.23},
    {"id": "SV002", "name": "Trần Thị Bích Ngọc", "age": 21, "gpa": 17.12},
    {"id": "SV003", "name": "Lê Văn Hùng", "age": 22, "gpa": 14.67},
    {"id": "SV004", "name": "Phạm Minh Tuấn", "age": 20, "gpa": 11.43},
    {"id": "SV005", "name": "Vũ Thị Hòa", "age": 23, "gpa": 12.89},
    {"id": "SV006", "name": "Đỗ Quốc Khánh", "age": 19, "gpa": 8.79},
    {"id": "SV007", "name": "Nguyễn Thị Mai", "age": 21, "gpa": 9.99},
    {"id": "SV011", "name": "Dương Nhật Nam", "age": 19, "gpa": 15.99},
    {"id": "SV008", "name": "Bùi Văn Nam", "age": 22, "gpa": 12.45},
    {"id": "SV009", "name": "Hoàng Thị Thu Trang", "age": 20, "gpa": 4.08},
    {"id": "SV010", "name": "Trịnh Văn Cường", "age": 23, "gpa": 15.5},
]

count = 0
for student in students :
    count = count + 1
    print_students(student, count)

# Find the students with the highest and lowest scores.
GPA = []
for student in students:
    n = student["gpa"]
    GPA.append(n)

highest = biggest_integer(GPA)
lowest = smallest_integer(GPA)

print("\nThe top student(s) is/are :")
for student in students:
    if student["gpa"] == highest:
        print(" " * 3 + f"{student['name']:<15}, with the score : {highest}")

print("\nThe bottom student(s) is/are :")
for student in students:
    if student["gpa"] == lowest:
        print(" " * 3 + f"{student['name']:<15}, with the score : {lowest}")

# Classify gpa 
GPA_students = []
for student in students :
    GPA.append(student['gpa'])
    for i in range(len(GPA)) :
        for j in range(i + 1, len(GPA)) :
            if GPA[i] >= GPA[j] :
                temp = GPA[i]
                GPA[i] = GPA[j]
                GPA[j] = temp

print("\nList of GPA: ", GPA)