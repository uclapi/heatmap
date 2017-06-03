import requests
from helpers import get_points_for_bookings, convertToGeoJSON

# Write your code here

UCL_API_TOKEN =


req = requests.get(
    "https://uclapi.com/roombookings/rooms",
    params={
        "token": UCL_API_TOKEN
    }
)

rooms = req.json()["rooms"]

req = requests.get(
    "https://uclapi.com/roombookings/bookings",
    params={
        "token": UCL_API_TOKEN,
        "date": "20170602"
    }
)

# Don't change lines below

points = get_points_for_bookings(bookings, rooms)

geojson_output = convertToGeoJSON(points)

with open('bookings.geojson', 'w') as f:
    f.write(geojson_output)
