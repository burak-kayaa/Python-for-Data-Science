from typing import Any


def ft_median(numbers: list[float]) -> float:
    """Calculates the median of a list of numbers"""
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    return median


def calculate_quartile(numbers: list[float], percentile: float) -> float:
    """Calculates the given quartile (percentile) of a list of numbers"""
    numbers.sort()
    n = len(numbers)
    index = percentile * (n - 1)

    if index.is_integer():
        return numbers[int(index)]
    else:
        lower_index = int(index)
        upper_index = lower_index + 1
        fraction = index - lower_index
        return numbers[lower_index] * (1 - fraction) \
            + numbers[upper_index] * fraction


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates the statistics of a list of numbers

    Args:
        *args: A list of numbers
        **kwargs: A dictionary with the statistics to calculate
    """
    numbers = list(args)
    mean = sum(numbers) / len(numbers) if numbers else 0

    for key, value in kwargs.items():
        if not args:
            print("ERROR")
            continue
        if value == "median":
            median = ft_median(numbers)
            print(f"Median: {median}")
        elif value == "mean":
            print(f"Mean: {mean}")
        elif value == "quartile":
            quartile_25 = calculate_quartile(numbers, 0.25)
            quartile_75 = calculate_quartile(numbers, 0.75)
            quartiles = [quartile_25, quartile_75]
            print(quartiles)
        elif value == "std":
            std = (sum([(x - mean) ** 2 for x in numbers])
                   / len(numbers)) ** 0.5
            print(f"std : {std}")
        elif value == "var":
            var = sum([(x - mean) ** 2 for x in numbers]) / len(numbers)
            print(f"var : {var}")
        else:
            pass
