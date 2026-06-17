import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.candidate_station_service import (
    CandidateStationService
)

service = CandidateStationService()

stations = service.get_cheapest_by_state(
    ["TX", "OK", "MO", "IL"]
)

print(
    stations[
        [
            "State",
            "Truckstop Name",
            "City",
            "Retail Price"
        ]
    ]
)