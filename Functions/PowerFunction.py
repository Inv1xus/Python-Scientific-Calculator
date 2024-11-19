def power(x,y):

    #this is the case where y is 0 and any number to the power of 0 is 1
    if y == 0:
        return 1


    #this the case where the x is 0 and the answer will always be 0 unless the y is negative in which case the answer is undefined
    if x == 0:
        if y > 0:
            return 0
        else:
            raise ValueError("0 raised to a negative power is undefined!")

    # handle the most common case where the y is positive
    if y > 0:
        result = 1
        for _ in range(int(y)):  # multiplies x by itself y times
            result *= x
        return result

    # this is the case where y is negative
    if y < 0:
        result = 1
        for _ in range(int(-y)):  # multiplies x by itself -y times
            result *= x
        return 1 / result



