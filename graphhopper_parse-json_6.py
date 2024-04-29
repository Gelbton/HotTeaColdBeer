import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "graphhopper_key"

def geocoding(vehicle, to, destination):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": to, "limit": "1", "key": key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": destination, "limit": "1", "key": key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
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
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)

    else:
        lat = "null"
        lng = "null"
        new_loc = "null"
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])

    return json_status, lat, lng, new_loc

    # def geocoding (location, key):
    #     while location == "":
    #         location = input("Enter the location again: ")
    #     geocode_url = "https://graphhopper.com/api/1/geocode?"
    #     url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})
    #     replydata = requests.get(url)
    #     json_data = replydata.json()
    #     json_status = replydata.status_code
    #     json_status = replydata.status_code
        
    #     geocode_url = "https://graphhopper.com/api/1/geocode?"
    #     url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1",
    #     "key":key})
    #     replydata = requests.get(url)
    #     json_data = replydata.json()
    #     json_status = replydata.status_code
    #     if json_status == 200 and len(json_data["hits"]) !=0:
    #         lat = json_data["hits"][0]["point"]["lat"]
    #         lng = json_data["hits"][0]["point"]["lng"]
    #         name = json_data["hits"][0]["name"]

    #         value = json_data["hits"][0]["osm_value"]
    #         if "country" in json_data["hits"][0]:
    #             country = json_data["hits"][0]["country"]
    #         else:
    #             country=""
    #         if "state" in json_data["hits"][0]:
    #             state = json_data["hits"][0]["state"]
    #         else:
    #             state=""
    #         if len(state) !=0 and len(country) !=0:
    #             new_loc = name + ", " + state + ", " + country
    #         elif len(state) !=0:
    #             new_loc = name + ", " + country
    #         else:
    #             new_loc = name
    #         print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n"+ url)
                
    #     else:
    #         lat="null"
    #         lng="null"
    #         new_loc=location
    #         if json_status != 200:
    #             print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])
            
    #     return json_status,lat,lng,new_loc
    