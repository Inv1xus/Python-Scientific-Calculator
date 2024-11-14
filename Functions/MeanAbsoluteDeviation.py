def mean_absolute_deviation(data):
    """
    Calculate the Mean Absolute Deviation (MAD) of a list of numerical data points.

    Parameters:
    data (list of float): List of numerical data points.

    Returns:
    float: The Mean Absolute Deviation of the data.
    """
    # Step 1: Calculate the mean (μ)
    mean = sum(data) / len(data)
    
    # Step 2: Calculate the absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in data]
    
    # Step 3: Calculate the mean of these absolute deviations
    mad = sum(absolute_deviations) / len(data)
    
    return mad
