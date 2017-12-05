# CTI 110
# M6HW1 - Test Average and Grades
# Chanell Custodio
# 12/5/17
# Displays letter grade (from given # grade) and calculates the average test score


AMOUNT_OF_SCORES = 5


# Adds each score together and divides by the constant, 5
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / AMOUNT_OF_SCORES
    return average

# Determines the letter grade based on the number score using if statements
def determine_grade(score):
    if(score < 60):
        return 'F'
    elif(score < 70):
        return 'D'
    elif(score < 80):
        return 'C'
    elif(score < 90):
        return 'B'
    elif(score < 101):
        return 'A'

# Asks user for each of the 5 number grades
def get_scores():
    score1 = float(input('Please enter the first score: '))
    score2 = float(input('Please enter the next score: '))
    score3 = float(input('Please enter the next score: '))
    score4 = float(input('Please enter the next score: '))
    score5 = float(input('Please enter the last score: '))

    return score1, score2, score3, score4, score5

# Displays the number scores and their corresponding letter grades
def print_table_of_results(score1, score2, score3, score4, score5):
    print('Score:     Letter Grade:')
    print(str(score1) + '       ' + determine_grade(score1))
    print(str(score2) + '       ' + determine_grade(score2))
    print(str(score3) + '       ' + determine_grade(score3))
    print(str(score4) + '       ' + determine_grade(score4))
    print(str(score5) + '       ' + determine_grade(score5))

# Calls the other functions and displays the average score
def main():
    score1, score2, score3, score4, score5 = get_scores()
    print_table_of_results(score1, score2, score3, score4, score5)

    print('Your average is: ',calc_average(score1, score2, score3, score4, score5))


# Run program
main()
