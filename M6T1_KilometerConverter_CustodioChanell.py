# CTI 110
# M6T1 - Kilometer Converter
# Chanell Custodio
# 11/28/17
# Convert kilometers to miles using input from user


CONVERSION_FACTOR = 0.6214

          
def main():

    # Get distance amount in kilometers from user
    kilometers = float(input('Enter a distance in Kilometers: '))

    # Display conversion of kilometers to miles
    show_miles(kilometers)


def show_miles(km):
    
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')




# Call the main function
main()
