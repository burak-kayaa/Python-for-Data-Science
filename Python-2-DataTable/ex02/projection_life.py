from load_csv import load
from matplotlib import pyplot as plt


def string_to_int(value: str) -> int:
    """
    Remove 'M' from a string like '1.27M' and convert it to an integer.

    Parameters:
    ----------
    value : str
        The string containing a number with 'M' (for millions).

    Returns:
    ----------
    int
        The converted integer value.
    """
    if 'M' in value:
        numeric_value = float(value.replace('M', ''))
        return int(numeric_value * 1_000_000)
    elif 'K' in value:
        numeric_value = float(value.replace('K', ''))
        return int(numeric_value * 1_000)
    else:
        return int(value)


def main():
    """
    Load the life expectancy dataset
    and plot life expectancy for Turkey and France.
    """
    df = load("population_total.csv")
    if df is None:
        return None
    turkey_data = df[df['country'] == 'Turkey']
    turkey_data = turkey_data.drop(columns='country').T
    turkey_data.columns = ['population']
    turkey_data['year'] = turkey_data.index.astype(int)
    turkey_data = turkey_data[(turkey_data['year'] >= 1800)
                              & (turkey_data['year'] <= 2050)]
    turkey_data['population'] = turkey_data['population'].apply(string_to_int)

    france_data = df[df['country'] == 'France']
    france_data = france_data.drop(columns='country').T
    france_data.columns = ['population']
    france_data['year'] = france_data.index.astype(int)
    france_data = france_data[(france_data['year'] >= 1800)
                              & (france_data['year'] <= 2050)]
    france_data['population'] = france_data['population'].apply(string_to_int)
    try:
        plt.plot(turkey_data['year'],
                 turkey_data['population'], label='Turkey')
        plt.plot(france_data['year'],
                 france_data['population'], label='France')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population in Turkey and France')
        plt.legend()
        plt.show()
    except KeyboardInterrupt:
        print("Plotting cancelled by user")
        return None


if __name__ == '__main__':
    main()
