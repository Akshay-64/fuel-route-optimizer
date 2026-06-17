from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from routing.serializers import (
    RouteOptimizationSerializer
)

from routing.services.geocoding_service import (
    GeocodingService
)

from routing.services.route_service import (
    RouteService
)

from routing.services.fuel_optimizer_service import (
    FuelOptimizerService
)


class RouteOptimizationView(APIView):

    def post(self, request):

        serializer = (
            RouteOptimizationSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        start = serializer.validated_data["start"]

        finish = serializer.validated_data["finish"]

        route_states = serializer.validated_data[
            "route_states"
        ]

        geocoding_service = (
            GeocodingService()
        )

        start_coordinates = (
            geocoding_service.get_coordinates(
                start
            )
        )

        finish_coordinates = (
            geocoding_service.get_coordinates(
                finish
            )
        )

        route_service = RouteService()

        route = route_service.get_route(
            start_coordinates,
            finish_coordinates
        )

        distance_miles = round(
            route["distance_meters"]
            * 0.000621371,
            2
        )

        duration_hours = round(
            route["duration_seconds"]
            / 3600,
            2
        )

        optimizer = (
            FuelOptimizerService()
        )

        optimization_result = (
            optimizer.optimize(
                distance_miles=distance_miles,
                route_states=route_states
            )
        )

        return Response(
            {
                "start": start,
                "finish": finish,
                "distance_miles": distance_miles,
                "duration_hours": duration_hours,
                "gallons_needed":
                    optimization_result[
                        "gallons_needed"
                    ],
                "total_cost":
                    optimization_result[
                        "total_cost"
                    ],
                "fuel_stops":
                    optimization_result[
                        "fuel_stops"
                    ]
            },
            status=status.HTTP_200_OK
        )