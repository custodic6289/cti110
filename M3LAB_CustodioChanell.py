# CTI 110
# M3LAB - Debugging
# Chanell Custodio
# 9/28/17
# Debug the incorrect code so it effectively inputs number grade and ouputs a letter grade

def main():

    # System uses a 10-point grading scale
    # Letter score = number score
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    score = int(input('Enter number grade: '))
'''
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    if score >= F_score:
                        print('Your grade is: F')
                    else:
                        if score <= F_score:
                            print('Your grade is: F')
'''
def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    score = int(input('Enter number grade: '))
    
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')    
    elif score >= D_score:
        print('Your grade is: D') 
    else: 
        print('Your score is: F')
        
# Program start and run 6 times
main()
main()
main()
main()
main()
main()

    
    
    
