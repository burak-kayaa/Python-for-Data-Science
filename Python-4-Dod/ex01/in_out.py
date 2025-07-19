def square(x: int | float) -> int | float:
    """Returns the square of a number"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the power of a number"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that calculates the result of a given function
    with the previous result

    Args:
        x: The initial value
        function: The function to use

    Returns:
        The inner function
    """
    def inner() -> float:
        """
        Returns the result of the given function with the previous result

        Returns:
            The result of the function
        """
        nonlocal x
        x = function(x)
        return x
    return inner
