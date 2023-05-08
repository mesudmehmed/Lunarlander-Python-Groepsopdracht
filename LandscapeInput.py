"""
In this file the basic shape of a created landscape is imported.

To create a landscape:
- We need x- and y- coordinates of points which determine the global shape of the landscape.
- Also see the file 'Landscape_Creation_Instruction.docx'

- Open paint and make the size of it as big as the game screen size
- Draw a landscape of straight lines (mind about drawing a horizontal line to locate the finish-field)
- Draw points at every start and end of lines
- In this game, we call these points 'big points'
- When holding the cursor above these points, one can read the pixel location, left below at the screen
- These two values are decided to be 'x and y coordinates' for the 'big points'
- For all 'big points', put these values in the file using this link:
https://docs.google.com/spreadsheets/d/1SxisOetj0AnPPhx1MVw0TZj_P1YSMi0h8uvHao3xMo0/edit?usp=sharing

- For now, one can put 'ones' in column 'n_intervals' and 'zeros' in column 'max_amplitudes',
- Both these lists are one item shorter than the lists 'big_points'/'x_coordinates'/'y_coordinates',
    since these correspond with the lines in between the 'big points'.
- In the file 'LandscapeShaper' you can find more information on what 'n_intervals' and 'max_amplitudes' are used for.
- Download the file as CSV-file to the same directory where you run the game.
- Give the file a name and copy it to the 'landscape'-variable in 'main'

In the code below, the data in this CSV-file is imported.
"""

# Import
import csv

# X & Y COO. OF BIG POINTS ############################ (LANDSCAPE) #
# Getting x and y coordinates of 'big points',
# Getting number of intervals in between every 'big point' and the next one,
# Getting maximum amplitude of small points relative to 'imaginary big line' in between two big points

def get_big_points_and_else(landscape_file_name):

    lines = []
    with open(landscape_file_name) as csv_file:  # open file
        csv_reader = csv.reader(csv_file, delimiter=',')  # read file
        for line in csv_reader:
            lines.append(line)  # make lists of lists

    headers = lines[0]  # headers
    data = lines[1:]  # data

    big_x_coordinates = []
    big_y_coordinates = []
    n_intervals = []
    max_amplitudes = []
    finish_field_x = []
    finish_field_y = []

    k = 0
    for row in data:
        k += 1
        if k == len(
                data):  # for last row of data, only process x_coo and y_coo since n_intervals and max_amplitudes are already done being processed (one item less)
            big_x_coordinates.append(int(row[1]))  # add x coordinate
            big_y_coordinates.append(int(row[2]))  # add y coordinate

        else:
            big_x_coordinates.append(int(row[1]))  # add x coordinate
            big_y_coordinates.append(int(row[2]))  # add y coordinate
            n_intervals.append(int(row[3]))  # add n_interval
            max_amplitudes.append(int(row[4]))  # add max_amplitude
            if not row[5] == '':
                finish_field_x.append(int(row[1]))
                finish_field_y.append(int(row[2]))


    return big_x_coordinates, big_y_coordinates, n_intervals, max_amplitudes, finish_field_x, finish_field_y