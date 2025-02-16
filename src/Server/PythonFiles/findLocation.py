from geopy.geocoders import Nominatim

def getLocation(location):
    geolocator = Nominatim(user_agent='myapplication')
    location1 = geolocator.geocode(location)
    return(float(location1.raw["lat"]), float(location1.raw["lon"]))

if __name__ == "__main__":
    getLocation("Edmonton")
