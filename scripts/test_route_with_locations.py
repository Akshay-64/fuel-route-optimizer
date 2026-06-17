import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.geocoding_service import GeocodingService
from routing.services.route_service import RouteService


def meters_to_miles(meters):
    return round(meters * 0.000621371, 2)


def seconds_to_hours(seconds):
    return round(seconds / 3600, 2)


geo = GeocodingService()
route_service = RouteService()

start = geo.get_coordinates("Dallas, TX")
finish = geo.get_coordinates("Chicago, IL")

route = route_service.get_route(
    start,
    finish,
)

print("\nRoute With Location Names")
print("-" * 50)

print(f"Start Coordinates : {start}")
print(f"End Coordinates   : {finish}")

print(
    f"Distance          : "
    f"{meters_to_miles(route['distance_meters'])} miles"
)

print(
    f"Duration          : "
    f"{seconds_to_hours(route['duration_seconds'])} hours"
)

print(
    f"Geometry Points   : "
    f"{len(route['geometry']['coordinates'])}"
)