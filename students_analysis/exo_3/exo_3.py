students = [
    {"id": "SV001", "name": "Nguyễn Văn An", "age": 20, "gpa": 17.12},
    {"id": "SV002", "name": "Trần Thị Bích Ngọc", "age": 21, "gpa": 17.12},
    {"id": "SV003", "name": "Lê Văn Hùng", "age": 22, "gpa": '14.67'},
    {"id": "SV004", "name": "Phạm Minh Tuấn", "age": 20, "gpa": 17.12},
    {"id": "SV005", "name": "Vũ Thị Hòa", "age": 23, "gpa": 12.89},
    {"id": "SV006", "name": "Đỗ Quốc Khánh", "age": 19, "gpa": ' '},
    {"id": "SV007", "name": "Nguyễn Thị Mai", "age": 21, "gpa": 9.99},
    {"id": "SV011", "name": "Dương Nhật Nam", "age": 19, "gpa": 15.99},
    {"id": "SV008", "name": "Bùi Văn Nam", "age": 22, "gpa": 'abc'},
    {"id": "SV009", "name": "Hoàng Thị Thu Trang", "age": 20, "gpa": 4.08},
    {"id": "SV010", "name": "Trịnh Văn Cường", "age": 23, "gpa": 15.5},
]

## === Sort students by the validity of GPA (it must be a number) ===
list_invalid = []
students_valid = []

for student in students:
    gpa = student['gpa']
    if isinstance(gpa, str):
        gpa = gpa.strip()  # erase white space
        if gpa.replace('.', '', 1).isdigit(): # if number 
            student['gpa'] = float(gpa)
            students_valid.append(student)
        else: # if not number
            list_invalid.append(student)
    else:
        students_valid.append(student)

## === Sort students after having their GPA sorted ===
for i in range(len(students_valid)):
    for j in range(i + 1, len(students_valid)):
        # Compare GPA (float)
        if students_valid[i]['gpa'] < students_valid[j]['gpa']:
            temp = students_valid[i]
            students_valid[i] = students_valid[j]
            students_valid[j] = temp

        # if GPA identical, compare age (lower age prioritized)
        elif students_valid[i]['gpa'] == students_valid[j]['gpa']:
            if students_valid[i]['age'] > students_valid[j]['age']:
                temp2 = students_valid[i]
                students_valid[i] = students_valid[j]
                students_valid[j] = temp2
            elif students_valid[j]['age'] == students_valid[i]['age']:
                name_i = students_valid[i]['name'].split()[-1].lower()[0] 
                name_j = students_valid[j]['name'].split()[-1].lower()[0] 
                if name_i > name_j: # from a to z
                    students_valid[i], students_valid[j] = students_valid[j], students_valid[i] 
                    # shorter way to change position

## === Put the invalid students to the bottom of the list ===
for s in list_invalid:
    students_valid.append(s)

## === Print the result ===
for student in students_valid:
    print(student)

