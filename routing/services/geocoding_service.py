import requests


class GeocodingService:

    BASE_URL = "https://nominatim.openstreetmap.org/search"

    def get_location_data(
        self,
        location
    ):

        response = requests.get(
            self.BASE_URL,
            params={
                "q": location,
                "format": "jsonv2",
                "addressdetails": 1,
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

        return data[0]

    def validate_us_location(
        self,
        location_data
    ):

        address = location_data.get(
            "address",
            {}
        )

        country = (
            address.get(
                "country",
                ""
            )
            .strip()
            .lower()
        )

        return country in [
            "united states",
            "united states of america",
        ]

    def get_coordinates(
        self,
        location
    ):

        result = self.get_location_data(
            location
        )

        if not self.validate_us_location(
            result
        ):
            raise ValueError(
                f"Location must be within the USA: {location}"
            )

        return (
            float(result["lon"]),
            float(result["lat"]),
        )