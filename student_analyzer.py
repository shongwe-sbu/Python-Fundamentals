def find_highest(marks):
    
    highest_mark = marks[0]
    for mark in marks:
        if mark > highest_mark:
            highest_mark = mark
    return highest_mark

def calculate_average(marks):
    
    total = 0
    for mark in marks:
        total = total + mark
    total = total / len(marks) 
    return total

def count_passes(marks):
    
    count = 0
    for mark in marks:
        if mark >= 50:
            count += 1
    return count

class_marks = [45, 88, 72, 91, 55, 30, 60]

print(f"Class Average:{calculate_average(class_marks)} Highest Mark:{find_highest(class_marks)} Students Passed:{count_passes(class_marks)}")