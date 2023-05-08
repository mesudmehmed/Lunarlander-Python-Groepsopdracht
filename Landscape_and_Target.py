

def getLandscape_and_Target(landscape, win_width):

    # Landscape
    # Choose here which landscape should be imported

    # landscape = 'landscape_default'  # aanhalingstekens niet vergeten
    landscape_file_name = landscape + '.csv'

    # LandscapeInput
    from LandscapeInput import get_big_points_and_else

    big_x_coordinates, big_y_coordinates, n_intervals, max_amplitudes, finish_field_x, finish_field_y = get_big_points_and_else(
        landscape_file_name)

    # LandscapeShaper
    from LandscapeShaper import determine_small_points
    from LandscapeShaper import get_dots
    from LandscapeShaper import find_corners
    from LandscapeShaper import double_corners
    from LandscapeShaper import get_all_y_at_x_sorted_with_minus_one

    # determine coordinates small points
    small_x_coordinates, small_y_coordinates = determine_small_points(big_x_coordinates, big_y_coordinates, n_intervals,
                                                                      max_amplitudes)

    # get dots
    dots_x, dots_y = get_dots(small_x_coordinates, small_y_coordinates)

    # find and double corners
    corners_index = find_corners(dots_x)
    dots_x, dots_y = double_corners(corners_index, dots_x, dots_y)

    # determine all y's at each x, add 'minus one' and sort
    all_y_at_x_sorted_with_minus_one = get_all_y_at_x_sorted_with_minus_one(win_width, dots_x, dots_y)

    # Target
    # waarde van target bepalen
    targetWidth = 64
    targetHeight = 64
    target_left_X = finish_field_x[0]
    target_bottom_Y = finish_field_y[0]

    return small_x_coordinates, small_y_coordinates, dots_x, dots_y, all_y_at_x_sorted_with_minus_one, targetWidth, targetHeight, target_left_X, target_bottom_Y