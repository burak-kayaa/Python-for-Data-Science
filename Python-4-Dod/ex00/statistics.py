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

    if not args:
        for key in kwargs:
            print("ERROR")
        return
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("All arguments must be numbers")
    if not kwargs:
        print("No statistics requested. Please specify at least one statistic to calculate.")
    numbers = sorted(args)
    
    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(numbers) / len(numbers)
            print(f"Mean: {mean:.1f}")
        elif value == "median":
            median = ft_median(numbers)
            print(f"Median: {median}")
        elif value == "quartile":
            q25 = calculate_quartile(numbers, 0.25)
            q75 = calculate_quartile(numbers, 0.75)
            print(f"quartile : [{q25:.1f}, {q75:.1f}]")
        elif value == "std":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            std_dev = variance ** 0.5
            print(f"std: {std_dev:f}")
        elif value == "var":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            print(f"var: {variance:f}")
        else:
            continue