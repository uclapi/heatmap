import requests
from helpers import get_points_for_bookings, convertToGeoJSON

# Write your code here





# Don't change lines below

points = get_points_for_bookings(bookings, rooms)

geojson_output = convertToGeoJSON(points)

with open('bookings.geojson', 'w') as f:
    f.write(geojson_output)
