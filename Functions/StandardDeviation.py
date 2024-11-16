def standard_deviation(data):
    """
    Calculate the Standard Deviation (SD) of a list of numerical data points.

    Parameters:
    data (list of float): List of numerical data points.

    Returns:
    float: The Standard Deviation of the data.
    """
    # Step 1: Calculate the mean (μ)
    mean = sum(data) / len(data)
    
    # Step 2: Calculate the squared deviations from the mean
    squared_deviations = [(x - mean) ** 2 for x in data]
    
    # Step 3: Calculate the variance (mean of squared deviations)
    variance = sum(squared_deviations) / len(data)
    
    # Step 4: Take the square root of the variance to get the standard deviation
    std_dev = variance ** 0.5
    
    return std_dev

