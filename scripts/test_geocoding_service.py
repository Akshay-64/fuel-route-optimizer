import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)

from routing.services.geocoding_service import GeocodingService

service = GeocodingService()

coords = service.get_coordinates(
    "Dallas, TX"
)

print(coords)