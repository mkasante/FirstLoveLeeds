import requests

def getdata(origin, destination, mode="walking"):
    destinations = "|".join(destination)
    result = []

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + \
	origin + "&destinations=" + destinations + "&mode=" + mode + "&key=AIzaSyD68CJlpEQG9PvVvk95liARUfUuSfnSTy0"

    r = requests.get(url)
    data = r.json()
    
    for x in range(len(destination)):
        origin_address = str(data["origin_addresses"][0])
        dest_address = str(data["destination_addresses"][x])

        elements = data["rows"][0]["elements"][x]

        if dest_address != "":
            duration = elements['duration']["text"]
            distance = elements['distance']["text"]
            
            if distance.endswith(" m"):
                distance = float(distance.split(" m")[0]) * 0.001
            else:
                distance = float(distance.split(" km")[0])

        else:
            duration = distance = "unknown"

        result.append((origin_address, dest_address, duration, distance))

    return result