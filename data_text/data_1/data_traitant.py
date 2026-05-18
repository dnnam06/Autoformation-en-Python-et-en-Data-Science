from data_text.functions_data import change_format, read_info

lines = read_info('data_text/data_1/data.txt')
new_lines = change_format(lines)

with open('data_text/data_1/new_data.txt', "w", encoding="utf-8") as f:
        f.write(new_lines)