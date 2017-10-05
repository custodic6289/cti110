# CTI 110
# M3HW1 - Age Classifier
# Chanell Custodio
# 10/5/17
# Classify age by getting input from user and coverting it to a term


def main():

    # Define age variables:
    # infant = ages 0-1
    # child = ages 2-12
    # teenager = ages 13-19
    # adult = ages 20 and up

    # Get (number) age from user
    age = int(input('Enter the age: '))
    

    if age <= 1:
        print('This age classifies as an infant.')
    else:
        if age <= 12:
            print('This age classifies as a child.')
        else:
            if age < 20:
                print('This age classifies as a teenager.')
            else:
                if age >= 20:
                    print('This age classifies as an adult.')
    
    

# Call program 10 times    
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
