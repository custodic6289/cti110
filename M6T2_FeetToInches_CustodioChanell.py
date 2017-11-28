# CTI 110
# M6T2 - Feet to Inches
# Chanell Custodio
# 11/28/17
# Convert feet to inches using input from user


# Constant for the number of inches per foot (12 inches = 1 foot)
INCHES_PER_FOOT = 12


def main():
    # Get a number of feet from user
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
# The feet to inches function converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT


# Call the main function
main()
