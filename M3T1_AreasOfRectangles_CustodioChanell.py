# CTI 110
# M3T1 - Areas of Rectangles
# Chanell Custodio
# 9/26/17
# Find the areas of rectangles



# User input the length and width of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# User input the length and width of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of rectangle 1 and 2
area1 = length1 * width1
area2 = length2 * width2

# Find out which rectangle had a greater area, or if they have the same area
if area1 > area2:
    print('Rectangle 1 has the greatest area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
