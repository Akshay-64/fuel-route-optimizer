import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.route_service import RouteService


def meters_to_miles(meters):
    return round(meters * 0.000621371, 2)


def seconds_to_hours(seconds):
    return round(seconds / 3600, 2)


service = RouteService()

route = service.get_route(
    (-96.7970, 32.7767),  # Dallas
    (-87.6298, 41.8781),  # Chicago
)

print("\nRoute Results")
print("-" * 40)

print(
    f"Distance: {meters_to_miles(route['distance_meters'])} miles"
)

print(
    f"Duration: {seconds_to_hours(route['duration_seconds'])} hours"
)

print(
    f"Geometry Points: "
    f"{len(route['geometry']['coordinates'])}"
)