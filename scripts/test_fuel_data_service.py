import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.fuel_data_service import (
    FuelDataService
)

service = FuelDataService()

print()

print(
    "Total Stations:",
    service.get_total_stations()
)

print()

print(
    "States:",
    len(service.get_states())
)

print()

print(
    service.get_dataframe().head()
)