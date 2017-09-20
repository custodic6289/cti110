# CTI-110
# M2HW2 - Tip Tax Total
# Chanell Custodio
# 9/19/17
# Calculates the Tip Tax and Total



# Get the food cost from the user
food_cost = float(input('Enter the total cost of food: $'))

# Constant Variable: Food Cost
FOODCOST = food_cost

# Variable: Tip
tip = FOODCOST * 0.18

# Variable: Sales Tax
salesTax = FOODCOST * 0.07

# Variable: Total
total = FOODCOST + salesTax + tip


print('Tip: $', format(tip, ',.2f'))
print('Tax: $', format(salesTax, ',.2f'))
print('Total: $', format(total, ',.2f'))

