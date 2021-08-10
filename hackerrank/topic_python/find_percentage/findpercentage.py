def find_percentage(student_marks, query_name):

    avg = (sum(student_marks[query_name])) / len(student_marks[query_name])

    return f"{avg:.02f}"