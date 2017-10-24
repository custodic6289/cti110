# CTI 110
# M5T2 - Bug Collector
# Chanell Custodio
# 10/24/17
# Calculate total of the number of bugs collected over a 7 day period

def main():
    
    # Initialize the accumulator
    total = 0

    # Get the bugs collected for each day
    for day in range(1, 8):
        # Prompt the user
        print('Enter the bugs colected on day', day,':')

        # Input the number of bugs
        bugs = int(input())

        # Add bugs to total
        total = total + bugs

    # Display the total bugs
    print('You collected a total of', total, 'bugs.')




# Run program
main()
