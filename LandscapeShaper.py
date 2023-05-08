"""
In this file, the first function creates so called 'small points'.
The locations of these 'small points' eventually define the landscape,
    so these hold all information there is about the landscape.
All other functions are there to process this into other useful information.

'Small Points'
- 'Small points' are created to add some 'randomness' to the landscape.
- Also see the file 'Landscape_Creation_Instruction.docx'

- 'Small points' are located in between every two 'big points'
- Every two 'big points' have a line in between
- This line is divided into a number of intervals
- This number is chosen in the column 'n_intervals' in the file: 'landscape_default.csv'
- This file can be created using the link below:
https://docs.google.com/spreadsheets/d/1SxisOetj0AnPPhx1MVw0TZj_P1YSMi0h8uvHao3xMo0/edit?usp=sharing
- Looking at the intervals again; at the start and at the end of every interval, a 'small point' is created.
- Next, every 'small point' (that isn't located at a 'big point'), is moved up or down
- This movement is limited by 'max_amplitude', but apart from that, it is random.
- 'max_amplitude' is again chosen in the column 'max_amplitudes' in the file: 'landscape_default.csv'
- The 'small points' are moved up and down randomly, since in reality landscapes also have a bit of random altitude
- For all 'small points', the x- and y- coordinates are determined now.
"""

# Import
import random

# X & Y COO. OF SMALL POINTS ########################## (LANDSCAPE) #
# Determining x and y coordinates for all 'small points'
def determine_small_points(big_x_coordinates,big_y_coordinates,n_intervals,max_amplitudes):

    small_x_coordinates = []
    small_y_coordinates = []

    for i in range(len(big_x_coordinates) - 1):  # For every 'big point' at the start of a 'imaginary big line'
        for j in range(n_intervals[
                           i]):  # For every 'small point' at the start of an interval, being part of a certain 'imaginary big line'
            if j == 0:  # If a 'small point' coincides with a 'big point'
                small_x_coordinates.append(big_x_coordinates[i])  # Assign x coordinate
                small_y_coordinates.append(big_y_coordinates[i])  # Assign y coordinate
            else:  # If a 'small point' doesn't coincide with a 'big point'
                small_x_coordinates.append(int(  # Assign x coordinate
                    big_x_coordinates[i] +
                    j * (big_x_coordinates[i + 1] - big_x_coordinates[i]) / n_intervals[i]
                ))
                small_y_coordinates.append(int(  # Assign y coordinate including random amplitude
                    big_y_coordinates[i] +
                    j * (big_y_coordinates[i + 1] - big_y_coordinates[i]) / n_intervals[i]
                    + (2 * random.random() - 1) * max_amplitudes[i]
                ))

    small_x_coordinates.append(
        big_x_coordinates[len(big_x_coordinates) - 1])  # Assign x coordinate to last 'small point'
    small_y_coordinates.append(
        big_y_coordinates[len(big_x_coordinates) - 1])  # Assign y coordinate to last 'small point'

    return small_x_coordinates,small_y_coordinates

# X & Y COO. OF DOTS ################################## (LANDSCAPE) #
# Determing x and y coordinates for all 'dots' being part of every 'small line'
def get_dots(small_x_coordinates,small_y_coordinates):

    dots_x = []
    dots_y = []

    for i in range(len(small_x_coordinates) - 1):  # For every 'small point' at the start of a 'small line'
        for j in range(abs(small_x_coordinates[i + 1] - small_x_coordinates[i])):  # For every 'dot'
            if small_x_coordinates[i + 1] - small_x_coordinates[i] > 0:  # If 'small line' goes to the right
                dots_x.append(small_x_coordinates[i] + j)  # Assign x coordinate
                dots_y.append(int(small_y_coordinates[i] +
                                  j / (small_x_coordinates[i + 1] - small_x_coordinates[i])
                                  * (small_y_coordinates[i + 1] - small_y_coordinates[i])
                                  ))  # Assign y coordinate
            if small_x_coordinates[i + 1] - small_x_coordinates[i] < 0:  # If 'small line' goes to the left
                dots_x.append(small_x_coordinates[i] - j)  # Assign x coordinate
                dots_y.append(int(small_y_coordinates[i] +
                                  j / (small_x_coordinates[i] - small_x_coordinates[i + 1])
                                  * (small_y_coordinates[i + 1] - small_y_coordinates[i])
                                  ))  # Assign y coordinate

    dots_x.append(small_x_coordinates[len(small_x_coordinates) - 1])  # Assign x coordinate to last 'dot'
    dots_y.append(small_y_coordinates[len(small_y_coordinates) - 1])  # Assign y coordinate to last 'dot'

    return dots_x,dots_y

# CORNERS ############################################# (LANDSCAPE) #
# 'Dots' need to be doubled to have them twice instead of once
# Find corners
def find_corners(dots_x):
    corners_index = []
    for i in range(len(dots_x) - 2):  # For every first 'dot' of all three following-up dots
        if dots_x[i] == dots_x[
            i + 2]:  # If x_coo of first dot is equal to x_coo of third dot, then second dot must be a 'corner'
            corners_index.append(i + 1)  # Add index of corner
    return corners_index

# Double corners
def double_corners(corners_index,dots_x,dots_y):
    k = 0
    for i in range(len(corners_index)):  # For every corner
        dots_x.insert(corners_index[i] + k + 1, dots_x[corners_index[i] + k])  # Insert x_coo of doubled dot
        dots_y.insert(corners_index[i] + k + 1, dots_y[corners_index[i] + k])  # Insert y_coo of doubled dot
        k += 1
    return dots_x,dots_y

# all Y's @ X ############################################# (LANDSCAPE) #

def get_all_y_at_x_sorted_with_minus_one(win_width,dots_x,dots_y):
    all_y_at_x = []
    all_y_at_x_sorted = []
    all_y_at_x_sorted_with_minus_one = []

    for i in range(win_width + 1):  # For every possible x coordinate
        list = []
        for j in range(len(dots_x)):  # For every dot
            if dots_x[j] == i:  # If dot j has x coordinate i
                list.append(dots_y[j])  # Add to temporary list
        all_y_at_x.append(list)  # Add temporary list to matrix of all y at x, which won't be used
        list.sort()  # Sort temporary list
        list_with_minus_one = [-1] + list  # Add '-1' element to temporary list
        all_y_at_x_sorted.append(list)  # Add sorted temporary list to matrix of sorted y at x, which won't be used
        all_y_at_x_sorted_with_minus_one.append(list_with_minus_one)  # Add combined sorted temporary list to matrix of sorted y plus '-1' at x

    return all_y_at_x_sorted_with_minus_one






