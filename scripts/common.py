"""Common settings for the group project: Could the forecast have warned of extreme rain?"""

# Region box (latitude descends in forecast, ascends in CMORPH)
REGION_BOX = dict(
    latitude=slice(15, -5),    # 5N to 5S (Ethiopia, South Sudan, northern Uganda, western Kenya)
    longitude=slice(30, 45),   # 30E to 45E
)

# Towns: name, latitude, longitude
TOWNS = {
    "Addis Ababa": {"lat": 8.98, "lon": 38.74},
    "Nairobi": {"lat": -1.29, "lon": 36.82},
    "Juba": {"lat": 4.85, "lon": 31.58},
    "Kampala": {"lat": 0.32, "lon": 32.58},
}

# Forecast start dates (index in time array for jja2025 season)
# Check with: ds.time.values to see available dates
FORECAST_START_DATES = {
    "2025-07-16": 45,
    "2025-07-23": 46,
    "2025-07-30": 47,
    "2025-08-06": 48,
}

# Return periods (years)
RETURN_PERIODS = [2, 10, 50]

# Thresholds for Part B (mm in 24 h)
THRESHOLDS_MM = [10, 20, 50]

# Probability threshold for Part D risk map
PROBABILITY_THRESHOLD = 0.20

# Duration for extreme rainfall analysis
DURATION = "24hr"

# Data store settings
ENDPOINT = "https://data.source.coop"
BUCKET = "e4drr-project"
FORECAST_STORE = "forecasts/ecmwf-ifs-ea-swio-realized-v3/49r1-jja2025"
CMORPH_STORE = "observations/cmorph_rp_icechunk"
