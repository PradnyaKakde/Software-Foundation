def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 85:
        return 'A, You got the highest grade'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D, Just passed'
    else:
        return 'F, You have failed. Try harder next time.'