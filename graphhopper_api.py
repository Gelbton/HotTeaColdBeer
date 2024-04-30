import json
import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "335611ac-82ff-414b-8ec4-3cfc21fff7c9"


def geocoding(place):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": place, "limit": "1", "key": key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""
        if len(state) != 0 and len(country) != 0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) != 0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        print("Geocoding API URL for " + new_loc + "\n" + url)
    else:
        lat = "null"
        lng = "null"
        new_loc = "null"
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])
    return json_status, lat, lng, new_loc


def get_route(vehicle, start, destination):
    orig_status, orig_lat, orig_lng, orig_new_loc = geocoding(start)
    print("Geocoding API Status: " + str(orig_status))
    print("Starting Location: " + orig_new_loc)

    dest_status, dest_lat, dest_lng, dest_new_loc = geocoding(destination)
    print("Geocoding API Status: " + str(dest_status))
    print("Destination: " + dest_new_loc)

    if orig_status == 200 and dest_status == 200:
        op = "&point=" + str(orig_lat) + "%2C" + str(orig_lng)
        dp = "&point=" + str(dest_lat) + "%2C" + str(dest_lng)
        paths_url = route_url + urllib.parse.urlencode({"key": key, "vehicle": vehicle}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        route = {
            "status": paths_status,
            "url": paths_url,
            "origin": orig_new_loc,
            "destination": dest_new_loc,
            "sec": int(paths_data["paths"][0]["time"] / 1000 % 60),
            "min": int(paths_data["paths"][0]["time"] / 1000 / 60 % 60),
            "hr": int(paths_data["paths"][0]["time"] / 1000 / 60 / 60),
            "points": [{"lat": orig_lat, "long": orig_lng}, {"lat":dest_lat,"long":dest_lng}],
            "instructions": [],
        }
        if paths_status == 200:
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                route["instructions"].append({
                    "path": path,
                    "distance_km": round(distance / 1000, 2),
                    "distance_miles": round(distance / 1000 / 1.61, 2),
                })
        else:
            route["error_message"] = paths_data["message"]

        return json.dumps(route)
    else:
        print("Error: Unable to retrieve route information.")
