import requests


class GeocodingService:
    BASE_URL = "https://nominatim.openstreetmap.org/search"

    def get_coordinates(self, location):
        response = requests.get(
            self.BASE_URL,
            params={
                "q": location,
                "format": "json",
                "limit": 1,
            },
            headers={
                "User-Agent": "fuel-route-optimizer"
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            raise ValueError(
                f"Location not found: {location}"
            )

        result = data[0]

        return (
            float(result["lon"]),
            float(result["lat"]),
        )