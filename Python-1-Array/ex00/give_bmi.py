def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate Body Mass Index (BMI) values for given height and weight lists.

    This function computes the BMI for each corresponding pair of
    height and weight values provided in the input lists.
    The BMI is calculated using the formula:

        BMI = weight / (height^2)

    where:
    - weight is in kilograms (kg)
    - height is in meters (m)

    Parameters
    ----------
    height : list of int or float
        A list of height values (in meters).
    weight : list of int or float
        A list of weight values (in kilograms).
        The length of this list must match the `height` list.

    Returns
    -------
    list of float
        A list of BMI values corresponding to each height and weight pair.
        The resulting BMI values are typically float values.

    Raises
    ------
    ValueError
        If the lengths of the height and weight lists are not equal.
    """
    if len(height) != len(weight):
        raise ValueError("The length of height and weight list must be equal.")
    bmis = []
    for h, w in zip(height, weight):
        if h <= 1:
            raise ValueError("Height value must be greater than 1.")
        if w <= 30:
            raise ValueError("Weight value must be greater than 30.")
        bmis.append(w / h ** 2)
    return bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a limit for every element of bmi values giving
    as an argument. İf its bigger than limit its True else False

    Parameters
    ----------
    bmi : list of int or float
        bmi values to iterate
    limit : int
        limit value

    Returns
    -------
    A list of boolean
    """
    booleans = []

    for value in bmi:
        if value >= limit:
            booleans.append(True)
        else:
            booleans.append(False)
    return booleans
