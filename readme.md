# Fuel Route Optimizer

## Overview

Fuel Route Optimizer is a Django REST API that calculates cost-effective fuel stops for a road trip within the United States.

The API:

* Accepts a start and destination location
* Generates a route using a free routing service
* Identifies optimal fuel stops based on fuel prices
* Calculates fuel consumption and estimated fuel cost
* Returns trip distance and duration

---

## Features

* Route generation between two US locations
* Fuel stop recommendations
* Fuel cost estimation
* CSV-based fuel price analysis
* REST API using Django REST Framework

---

## Tech Stack

* Python 3.11
* Django
* Django REST Framework
* Pandas
* OSRM Routing API
* OpenStreetMap Nominatim Geocoding API

---

## Project Structure

```text
routing/
├── services/
│   ├── geocoding_service.py
│   ├── route_service.py
│   ├── fuel_data_service.py
│   ├── candidate_station_service.py
│   └── fuel_optimizer_service.py
├── serializers.py
├── urls.py
└── views.py

data/
└── fuel-prices-clean.csv

scripts/
└── test_*.py
```

## Assumptions

* Vehicle range is 500 miles per full tank.
* Vehicle fuel efficiency is 10 MPG.
* Fuel prices are sourced from the supplied CSV file.
* Route states are currently supplied in the API request.
* Cheapest stations within route states are selected as candidate fuel stops.

---

## Installation

Clone repository:

```bash
git clone <repository-url>
cd fuel-optimizer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
python manage.py runserver
```

---

## API Endpoint

### Optimize Route

**POST**

```text
/api/routes/optimize/
```

### Request

```json
{
  "start": "Dallas, TX",
  "finish": "Chicago, IL",
  "route_states": ["TX", "OK", "MO", "IL"]
}
```

### Response

```json
{
  "start": "Dallas, TX",
  "finish": "Chicago, IL",
  "distance_miles": 966.45,
  "duration_hours": 17.09,
  "gallons_needed": 96.65,
  "total_cost": 280.17,
  "fuel_stops": [
    {
      "truckstop_name": "RAPID ROBERTS #123",
      "city": "Springfield",
      "state": "MO",
      "retail_price": 2.899
    }
  ]
}
```

---

## Optimization Logic

1. Convert locations into coordinates using Nominatim.
2. Generate route using OSRM.
3. Calculate trip distance.
4. Determine required fuel stops using:

   * Vehicle Range = 500 miles
   * Fuel Efficiency = 10 MPG
5. Select cost-effective stations from the provided fuel dataset.
6. Calculate estimated fuel cost.

---

## Future Improvements

* Automatically derive route states from route geometry.
* Geocode all fuel stations for precise route matching.
* Add caching for frequently requested routes.
* Add database-backed spatial queries.
* Support different vehicle fuel efficiencies.

---

