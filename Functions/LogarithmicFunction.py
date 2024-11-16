def natural_log(x, terms=100):
    """
    Approximate the natural logarithm (ln) of x using a Taylor series expansion.
    
    Parameters:
    x (float): The number to compute the natural log for. Must be > 0.
    terms (int): The number of terms to use in the series. Higher values increase precision.

    Returns:
    float: Approximation of ln(x).
    """
    if x <= 0:
        raise ValueError("x must be greater than 0.")

    # Transform x for convergence: ln(x) = -ln(1/x) if x < 1
    if x < 1:
        return -natural_log(1 / x, terms)

    # Use ln(x) = 2 * sum((z^(2k - 1)) / (2k - 1)) for z = (x - 1) / (x + 1)
    z = (x - 1) / (x + 1)
    z_squared = z * z
    result = 0
    for k in range(1, terms + 1):
        term = (z ** (2 * k - 1)) / (2 * k - 1)
        result += term

    return 2 * result

def log_base_b(x, b, terms=100):
    """
    Compute the logarithm of x with base b without using math functions.

    Parameters:
    x (float): The number to compute the logarithm for. Must be > 0.
    b (float): The base of the logarithm. Must be > 0 and != 1.
    terms (int): The number of terms to use in the series approximation of ln.

    Returns:
    float: The logarithm of x to the base b.

    Raises:
    ValueError: If x <= 0, b <= 0, or b == 1.
    """
    if x <= 0:
        raise ValueError("x must be greater than 0.")
    if b <= 0 or b == 1:
        raise ValueError("Base b must be greater than 0 and not equal to 1.")

    # Compute ln(x) and ln(b) using the natural_log function
    ln_x = natural_log(x, terms)
    ln_b = natural_log(b, terms)

    return ln_x / ln_b