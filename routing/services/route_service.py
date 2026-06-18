"""
RouteService

Responsibilities:
- Generates routes between two coordinates.
- Uses the free OSRM routing service.
- Returns route distance, duration, and geometry.
- Only requires a single routing API call.
"""

import requests


class RouteService:
    BASE_URL = "https://router.project-osrm.org"

    def get_route(self, start, end):
        """
        start = (lon, lat)
        end = (lon, lat)
        """

        url = (
            f"{self.BASE_URL}/route/v1/driving/"
            f"{start[0]},{start[1]};"
            f"{end[0]},{end[1]}"
        )

        response = requests.get(
            url,
            params={
                "overview": "full",
                "geometries": "geojson"
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        route = data["routes"][0]

        return {
            "distance_meters": route["distance"],
            "duration_seconds": route["duration"],
            "geometry": route["geometry"]
        }