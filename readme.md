# Fuel Route Optimizer

## Overview

Fuel Route Optimizer is a Django REST API that calculates the most cost-effective fuel stops along a driving route within the United States.

Given a start location and a destination, the API:

* Calculates the driving route.
* Identifies fuel stations located along or near the route.
* Determines optimal refueling stops based on fuel prices.
* Supports multiple fuel stops for long-distance trips.
* Estimates total fuel cost assuming:

  * Vehicle range: 500 miles
  * Fuel efficiency: 10 MPG

The solution is designed to minimize external API usage and provide fast responses through route caching and local fuel price processing.

---

## Assignment Requirements

### Input

```json
{
  "start": "Atlanta, GA",
  "finish": "Chicago, IL"
}
```

### Output

```json
{
  "distance_miles": 715,
  "fuel_stops": [],
  "total_fuel_cost": 0,
  "route": {}
}
```

---

## Technology Stack

* Python 3.x
* Django 5.x
* Django REST Framework
* PostgreSQL
* Redis (Caching)
* Pandas
* Shapely
* OpenRouteService API

---

## Data Source

Fuel pricing data is provided through the supplied CSV file.

The dataset contains:

* Truckstop ID
* Truckstop Name
* Address
* City
* State
* Retail Fuel Price

Since geographic coordinates are not included, a preprocessing step will enrich the dataset with latitude and longitude information.

---

## Planned Architecture

```text
Client
   |
   v
Django REST API
   |
   +--> Route Service
   |        |
   |        +--> OpenRouteService
   |
   +--> Fuel Optimization Engine
   |
   +--> Fuel Price Dataset
   |
   +--> Redis Cache
```

---

## Fuel Optimization Strategy

Vehicle assumptions:

* Maximum range: 500 miles
* Fuel economy: 10 MPG

The application will:

1. Retrieve the route.
2. Identify fuel stations near the route.
3. Determine reachable stations within the current fuel range.
4. Select cost-effective refueling locations.
5. Calculate total fuel cost for the trip.

---

## Performance Considerations

* Route results will be cached.
* Fuel station data will be processed locally.
* Only one routing API call will be used per unique route whenever possible.
* Geocoding will occur during preprocessing rather than during route requests.

---

## Project Status

Current Phase:

* [x] Project Initialization
* [ ] Django Setup
* [ ] Routing API Integration
* [ ] Fuel Data Enrichment
* [ ] Fuel Optimization Engine
* [ ] API Development
* [ ] Testing
* [ ] Dockerization
* [ ] Loom Demonstration

---

## Repository Structure (Planned)

```text
fuel-route-optimizer/
│
├── fuel_route_optimizer/
├── routing/
├── data/
├── tests/
├── docker-compose.yml
├── requirements.txt
└── README.md
```


