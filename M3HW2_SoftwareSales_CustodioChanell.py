# CTI 110
# M3HW2 - Software Sales
# Chanell Custodio
# 10/10/17
# Display discount percentage and total cost based on quantity of purchase


def main():

    # Declare variables
    num_packs = int(input('Enter the amount of packages purchased: '))
    PRICE = 99
    subtotal = PRICE*num_packs
    

    # Define discount percentage based on input
    if num_packs <10:
        discount_rate = 0
    else:
        if num_packs <20:
            discount_rate = .10
            print('10% Discount applied')
        else:
            if num_packs <50:
                discount_rate = .20
                print('20% Discount applied')
            else:
                if num_packs <100:
                    discount_rate = .30
                    print('30% Discount applied')
                else:
                    discount_rate = .40
                    print('40% Discount applied')
         
         
    # Declare variables to calculate
    discount = (discount_rate*subtotal)
    total = (subtotal-discount)

    # Display results
    print('Your total is: $', format(total, ',.2f'))

    
# Call program 5 times
main()
main()
main()
main()
main()
