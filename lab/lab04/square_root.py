def square_root(num):
    """Calculate the square root with 0.000001 precision"""
    num = abs(num)

    low = 0
    high = num
    middle = num
    old_middle = -1
    iteration_count = 0

    accuracy = 0.000001 # changed the accuracy level
    while abs(old_middle - middle) > accuracy:
        old_middle = middle

        middle = (high + low) / 2 # dividing by four doesn't find the middle. it needs to find the average
        middle_squared = middle * middle #previously was calculated as middle * 2

        if middle_squared > num:
            high = middle #was previously incorrect, this should be "high". Creates a ceiling
        else:
            low = middle #previously set the bounds reversely, should be "low" not "high"

        iteration_count += 1

    return round(middle, 4), iteration_count
