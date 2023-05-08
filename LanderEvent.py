# Import
import math

# Define if lander has reached target
def HitTarget(playerX, playerY, target_left_X, target_bottom_Y):
    distance = math.sqrt(math.pow(playerX - target_left_X, 2) + (math.pow(playerY - target_bottom_Y, 2)))
    if distance < 40:
        return True
    else:
        return False

# Define collision if top of lander touches a 'ceiling' or bottom of lander touches a 'bottom'
def Collision(playerX,playerY,all_y_at_x_sorted_with_minus_one):
    bottomleft_lander_X = playerX           # Determine x coordinate bottom,left corner of lander
    bottomleft_lander_Y = playerY + 25      # Determine y coordinate bottom,left corner of lander

    k = 0
    for i in range(25):                     # For every x coordinate covered by lander
                                            # For every combination of ceiling and corresponding bottom below
        for j in range(len(all_y_at_x_sorted_with_minus_one[bottomleft_lander_X + i])//2):
                                            # If top,left corner of lander doesn't touch certain ceiling and
                                            # bottom,left corner of lander doesn't touch corresponding bottom
            if bottomleft_lander_Y - 25 > all_y_at_x_sorted_with_minus_one[bottomleft_lander_X + i][2*j]\
                and bottomleft_lander_Y < all_y_at_x_sorted_with_minus_one[bottomleft_lander_X + i][2*j+1]:
                k += 1                      # Add one

    if k == 25:                              # If for every covered x coordinate, the lander is in between a certain combination of ceiling and corresponding bottom
        return False                        # No collision
    else:
        return True                         # Collision


