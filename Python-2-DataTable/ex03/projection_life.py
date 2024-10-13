from load_csv import load
from matplotlib import pyplot as plt


def main():
    """
    Load the data from the csv files and plot the scatter plot of the
    """
    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    df_life = load("life_expectancy_years.csv")
    if df_income is None or df_life is None:
        return None
    income_1900 = df_income[['country', '1900']]
    life_1900 = df_life[['country', '1900']]

    merged = income_1900.merge(life_1900, on='country',
                               suffixes=('_income', '_life'))
    merged['1900_income'] = merged['1900_income']\
        .apply(lambda x: int(x) if x != '' else None)
    merged['1900_life'] = merged['1900_life']\
        .apply(lambda x: float(x) if x != '' else None)
    merged = merged.dropna()

    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(merged['1900_income'], merged['1900_life'])
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.title('1900')
        plt.show()
    except KeyboardInterrupt:
        print("Interrupted")
        return None


if __name__ == "__main__":
    main()
