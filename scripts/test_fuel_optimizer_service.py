import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.fuel_optimizer_service import (
    FuelOptimizerService
)

service = FuelOptimizerService()

result = service.optimize(
    distance_miles=966.45,
    route_states=[
        "TX",
        "OK",
        "MO",
        "IL"
    ]
)

print()

print("Gallons Needed:")
print(result["gallons_needed"])

print()

print("Total Cost:")
print(result["total_cost"])

print()

print("Fuel Stops:")
for stop in result["fuel_stops"]:
    print(
        stop["Truckstop Name"],
        stop["State"],
        stop["Retail Price"]
    )