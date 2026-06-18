"""
RouteOptimizationSerializer

Responsibilities:
- Validates incoming API requests.
- Ensures required fields are present.
- Accepts start location, finish location, and route states.
"""

from rest_framework import serializers


class RouteOptimizationSerializer(
    serializers.Serializer
):
    start = serializers.CharField()
    finish = serializers.CharField()

    route_states = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=["TX", "OK", "MO", "IL"]
    )