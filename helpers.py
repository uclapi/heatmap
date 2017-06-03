from geojson import Feature, Point, FeatureCollection


def get_room_location_by_ids(rooms, roomid, siteid):
    for room in rooms:
        if room["roomid"] == roomid and room["siteid"] == siteid:
            return [
                room["roomname"],
                room["location"]["coordinates"]["lat"],
                room["location"]["coordinates"]["lng"],
            ]


def get_points_for_bookings(bookings, rooms):
    points = []
    for booking in bookings:
        points.append(
            get_room_location_by_ids(
                rooms,
                booking["roomid"],
                booking["siteid"]
            )
        )
    return points


def convertToGeoJSON(q):
    f = []
    for (name, lat, lon) in q:
        # print(lat, lon)
        lat, lon = map(float, (lat, lon))
        f.append(
            Feature(
                geometry=Point((lon, lat)),
                properties={"name": name}
            )
        )
    return str(FeatureCollection(f))
