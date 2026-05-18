HEADERS_STUDENTS_VN = 'MSSV,Họ tên,Giới tính,Ngày sinh,Lớp,Ngành học,Email,SĐT,Địa chỉ,Điểm trung bình'
HEADERS_STUDENTS_FR = "ID,NomPrenom,Sexe,DateNaissance,Classe,Filière,Email,Téléphone,Adresse,gpa"

def change_format(lines: list):
    lines_formatted = []
    for line in lines: 
        line = line.strip()
        if line == '':
            line = line
        else:
            line = line[0].upper() + line[1:]

        lines_formatted.append(line)

    str_lines = ""
    for line in lines_formatted:
        str_lines += line + '\n'

    return str_lines

def read_info(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines :
        if line != "\n":
            new_lines.append(line)

    return new_lines

def ranking_students_age(students: list[dict]):
    invalid_students = []
    valid_students = []
    for item in students:
        if item['gpa'] == '':
            invalid_students.append(item)
        else:
            valid_students.append(item)
    
    students = valid_students

    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            # Comparer les moyennes 
            if students[i]['gpa'] < students[j]['gpa']:
                students[i], students[j] = students[j], students[i] 
            if students[i]['gpa'] == students[j]['gpa']:
                if students[i]['DateNaissance'][0:3] == '2002':
                    students[i], students[j] = students[j], students[i] 
    
    for student in invalid_students:
        students.append(student)

    return students

def convert_student_to_list_dicts(lines: list[str]):
    for line in lines:
        headers_vn = lines[0].replace('\n', '')
        headers = headers_vn.replace(HEADERS_STUDENTS_VN, HEADERS_STUDENTS_FR)
        headers = headers.split(',')

        rows = lines[1:]

        students = []
        for line in rows:
            values = line.replace('\n', '').split(",")
            if len(headers) > len(values):
                difference = len(headers) - len(values)
                for i in range(difference+1):
                    values.append('') 
            student = {headers[i]: values[i] for i in range(len(headers))}
            students.append(student)
    
    return students

def write_students_to_text(students: list[dict]):
    str_students = '' 
    for student in students:
        str_student = ''
        for key, value in student.items():
            str_student += str(value) + ','
        
        str_students += str_student.strip(' ')[:-1] + '\n'
    
    str_students = HEADERS_STUDENTS_FR + '\n' + str_students 

    with open('data/data_2/new_students.txt', "w", encoding="utf-8") as f:
        f.write(str_students)
 
def convert_student(students: list[dict]):
    a = []
    for student in students:
        s = convert_gpa(student['gpa'])
        student['gpa'] = s
        a.append(student)

    return a

def convert_gpa(x):
    if isinstance(x, str):
        x = x.replace('"', '')
        if x == '':
            return x 
        return float(x)

    return x