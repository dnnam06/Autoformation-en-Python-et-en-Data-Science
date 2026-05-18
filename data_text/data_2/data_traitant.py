from data_text.functions_data import read_info, convert_student_to_list_dicts, convert_student, ranking_students_age, write_students_to_text

lines = read_info('data_text/data_2/students_data.txt')
students = convert_student_to_list_dicts(lines)
new_students = convert_student(students)
new_students = ranking_students_age(new_students)
write_students_to_text(new_students)
