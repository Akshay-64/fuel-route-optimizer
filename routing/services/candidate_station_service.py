from routing.services.fuel_data_service import FuelDataService


class CandidateStationService:

    def __init__(self):
        self.df = FuelDataService().get_dataframe()

    def get_candidate_stations(
        self,
        route_states,
        limit=20
    ):

        candidates = self.df[
            self.df["State"].isin(route_states)
        ]

        candidates = candidates.sort_values(
            by="Retail Price"
        )

        return candidates.head(limit)

    def get_cheapest_by_state(
        self,
        route_states
    ):

        candidates = self.df[
            self.df["State"].isin(route_states)
        ]

        result = (
            candidates
            .sort_values("Retail Price")
            .groupby("State", as_index=False)
            .first()
        )

        return result