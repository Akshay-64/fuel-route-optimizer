import pandas as pd

INPUT_FILE = "data/fuel-prices-for-be-assessment.csv"
OUTPUT_FILE = "data/fuel-prices-clean.csv"

VALID_STATES = {
    "AL","AK","AZ","AR","CA","CO","CT","DE",
    "FL","GA","HI","ID","IL","IN","IA","KS",
    "KY","LA","ME","MD","MA","MI","MN","MS",
    "MO","MT","NE","NV","NH","NJ","NM","NY",
    "NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV",
    "WI","WY","DC"
}

df = pd.read_csv(INPUT_FILE)

print(f"Original rows: {len(df)}")

# Remove exact duplicates
df = df.drop_duplicates()

print(f"After removing duplicates: {len(df)}")

# Keep only US states
df = df[df["State"].isin(VALID_STATES)]

print(f"After state filtering: {len(df)}")

# Create address for future geocoding
df["full_address"] = (
    df["Address"].astype(str)
    + ", "
    + df["City"].astype(str)
    + ", "
    + df["State"].astype(str)
    + ", USA"
)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved to {OUTPUT_FILE}")