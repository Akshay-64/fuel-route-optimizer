import pandas as pd

df = pd.read_csv(
    "data/fuel-prices-for-be-assessment.csv"
)

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("\nPrice Statistics:")
print(df["Retail Price"].describe())

print("\nLowest Prices:")
print(
    df.sort_values("Retail Price")
      .head(10)
)

print("\nHighest Prices:")
print(
    df.sort_values(
        "Retail Price",
        ascending=False
    ).head(10)
)

print(
    df["OPIS Truckstop ID"]
    .nunique()
)