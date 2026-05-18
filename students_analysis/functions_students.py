def smallest_integer(list) :
    small = list[0]
    for i in range(1, len(list)) : # used for list with dict / for number in list : (used for list with str or int)
        if list[i] < small : # list[i] is a number
            small = list[i]
    return small

def biggest_integer(list) :
    big = list[0]
    for number in list :
        if number > big :
            big = number 
    return big

def ranking(moyenne) :
    if moyenne >= 16 : 
        return "Très bien"
    elif (moyenne >= 14) and (moyenne < 16) :
        return "Bien"
    elif (moyenne >= 12) and (moyenne < 14) :
        return "Assez bien"
    elif (moyenne >= 10) and (moyenne < 12) :
        return "Passable"
    else :
        return "Insuffisant"

def print_students(student, count) :
    n = f"{count}  {student['id']}    {student['name']:<20}     {student['age']:<5}   {student['gpa']}"
    m = ranking(student['gpa'])
    n = n + '   ' + m
    if (count > 0) and (count < 10) :
        print(f"0{n}")
    else : 
        print(f"{n}")