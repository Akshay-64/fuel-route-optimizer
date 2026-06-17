import math

from routing.services.candidate_station_service import (
    CandidateStationService
)


class FuelOptimizerService:

    MPG = 10
    MAX_RANGE_MILES = 500

    def __init__(self):
        self.station_service = CandidateStationService()

    def select_stops(
        self,
        stations,
        stops_needed
    ):
        if stops_needed == 0:
            return stations.iloc[0:0]

        states = stations["State"].tolist()

        selected_indexes = []

        for i in range(stops_needed):
            index = int(
                (i + 1)
                * len(states)
                / (stops_needed + 1)
            )

            selected_indexes.append(index)

        return stations.iloc[selected_indexes]

    def optimize(
        self,
        distance_miles,
        route_states
    ):

        stations = (
            self.station_service
            .get_cheapest_by_state(route_states)
            .sort_values("Retail Price")
        )

        stops_needed = max(
            0,
            math.ceil(
                distance_miles / self.MAX_RANGE_MILES
            ) - 1
        )

        selected_stops = self.select_stops(
            stations,
            stops_needed
        )

        gallons_needed = (
            distance_miles / self.MPG
        )

        average_price = (
            selected_stops["Retail Price"].mean()
            if len(selected_stops)
            else stations["Retail Price"].min()
        )

        total_cost = (
            gallons_needed * average_price
        )

        fuel_stops = []

        for _, row in selected_stops.iterrows():
            fuel_stops.append(
                {
                    "truckstop_name": row["Truckstop Name"],
                    "city": row["City"].strip(),
                    "state": row["State"],
                    "retail_price": round(
                        float(row["Retail Price"]),
                        3
                    ),
                }
            )

        return {
            "fuel_stops": fuel_stops,
            "gallons_needed": round(
                gallons_needed,
                2
            ),
            "total_cost": round(
                total_cost,
                2
            ),
        }