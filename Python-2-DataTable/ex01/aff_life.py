from load_csv import load
from matplotlib import pyplot as plt


def main():
    """
    Load the life expectancy dataset
    and plot Turkey's life expectancy over the years.
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        return None
    turkey_data = df[df['country'] == 'Turkey']
    turkey_data = turkey_data.drop(columns='country').T
    turkey_data.columns = ['life_expectancy']
    turkey_data['year'] = turkey_data.index.astype(int)
    try:
        plt.plot(turkey_data['year'], turkey_data['life_expectancy'])
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('Life Expectancy in Turkey')
        plt.show()
    except KeyboardInterrupt:
        print("Plotting cancelled by user")
        return None


if __name__ == "__main__":
    main()
