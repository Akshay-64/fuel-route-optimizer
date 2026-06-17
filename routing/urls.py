from django.urls import path

from routing.views import (
    RouteOptimizationView
)

urlpatterns = [
    path(
        "optimize/",
        RouteOptimizationView.as_view(),
        name="optimize-route"
    ),
]