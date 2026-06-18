from pathlib import Path
"""
FuelDataService

Responsibilities:
- Loads the supplied fuel price CSV.
- Cleans and prepares fuel station data.
- Creates a full address field for stations.
- Provides a reusable DataFrame for optimization logic.
"""


import pandas as pd


class FuelDataService:
    def __init__(self):
        csv_path = (
            Path(__file__)
            .resolve()
            .parent.parent.parent
            / "data"
            / "fuel-prices-clean.csv"
        )

        self.df = pd.read_csv(csv_path)

    def get_dataframe(self):
        return self.df

    def get_total_stations(self):
        return len(self.df)

    def get_states(self):
        return sorted(
            self.df["State"].unique().tolist()
        )