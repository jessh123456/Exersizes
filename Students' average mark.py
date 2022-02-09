mark_list = []
student_list = []
loop = "TRUE"  # this is to keep asking for names
while loop == "TRUE":
    name = input("Enter student's name or press [x] to exit\n:")
    if name == "x":
        highest_mark = max(mark_list)
        max_index = mark_list. index(highest_mark)
        highest_student = student_list[max_index]
        average_score = sum(mark_list) / len(mark_list)
        print(f"The highest ranking student is {highest_student} with a score "
              f"of {highest_mark}. The average score is {average_score}.")
        quit()
    student_list.append(name)
    mark = int(input("Enter student's mark (between 0-100)\n:"))
    while 100 < mark < 0:
        mark = input("Sorry that is an invalid score, please try again.\n:")
    mark_list.append(mark)
