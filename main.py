"""
Testing API:
    1. httpbin.org

Collection API:
    1. openweathermap.org
    2. EarthQuakes?
    3. Flight delay
    4. National Floods API

response.content    # Return the raw bytes of the data payload
response.text       # Return a string representation of the data payload
response.json()     # This method is convenient when the API returns JSON   (USE)
"""

import requests
import json
import urllib
import sys
import csv
import codecs

def notes():

    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    print("POST: ", json.dumps(response.json(), indent=4))

    response = requests.get('https://httpbin.org/get')
    print("GET: ", json.dumps(response.json(), indent=4))

    response = requests.get('https://httpbin.org/ip')
    print("IP: ", json.dumps(response.json(), indent=4))

    r = requests.put('https://httpbin.org/pu', data={'key': 'value'})   # Made a typo put -> pu. Added if statement to avoid errors
    print("r.status_code == requests.codes.ok", r.status_code == requests.codes.ok)
    if r.status_code == requests.codes.ok:
        print("Put: ", json.dumps(r.json(), indent=4))
        print("r.raise_for_status(): ", r.raise_for_status())

    r = requests.delete('https://httpbin.org/delete')
    print("Delete: ", json.dumps(r.json(), indent=4))

    r = requests.head('https://httpbin.org/get')
    print("Head: ", r)
    print("r.status_code == requests.codes.ok", r.status_code == requests.codes.ok)

    r = requests.options('https://httpbin.org/ge')  # Made a typo. get -> ge. Getting 404 instead of 200
    print("Options: ", r)
    print("r.status_code == requests.codes.ok", r.status_code == requests.codes.ok)
    #print("r.raise_for_status(): ", r.raise_for_status())

# Source: https://www.getambee.com/api/weather?utm_term=weather%20api%20free&utm_campaign=Weather+API&utm_source=adwords&utm_medium=ppc&hsa_acc=9773927819&hsa_cam=10878269195&hsa_grp=112779988011&hsa_ad=499364796434&hsa_src=g&hsa_tgt=kwd-310969983501&hsa_kw=weather%20api%20free&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwp9qZBhBkEiwAsYFsb0HTx3Ndaxx73ZMeLvGIz8VjnNHr-wlqHbiVtejvG852Gs-GYDojJRoCbBgQAvD_BwE
# Short: getambee.com
# First 50,000 calls & First 30 days - for free
def get_current_weather(location=None):

    if location is None:
        location = {"lat": "12.9889055", "lng": "77.574044"}

    API_KEY = "255af5e285845bde1eda5c5c7d7e915ed21b2b3fa4b2c90be6c541970d5d5d57"
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
    querystring = location

    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.dumps(response.json(), indent=4))

    weather_parameters = {"visibility": response.json()["data"]["visibility"],      # Use for solar panels / Flights
                          "cloudCover": response.json()["data"]["cloudCover"],      # Use for solar panels
                          "windSpeed": response.json()["data"]["windSpeed"],        # Use for wind damage
                          "temperature": response.json()["data"]["temperature"],    # Use for hot/cold tem damage
                          "summary": response.json()["data"]["summary"],            # Use to display summary
                          "humidity": response.json()["data"]["humidity"]}          # Use to check for a rain

    return weather_parameters


# Was created with Aeris Api Wizard, a tool that generates code
# According to your form filling (location, what data is needed, etc)
# INITIAL CODE AFTER GENERATION WAS NOT WORKING!!!
# First 1,000 calls are free
def get_current_weather_aeris():

    # request = urllib.request.urlopen(
    #     'https://api.aerisapi.com/conditions/oxford, england?format=json&from=5 days ago&plimit=4&filter=15min&fields=loc,periods.tempC,periods.humidity,periods.windSpeedKPH,periods.weather&client_id=[CLIENT_ID]&client_secret=[CLIENT_SECRET]')

    request = requests.request(method="GET", url="https://api.aerisapi.com/conditions/oxford, england?format=json&from=5 days ago&plimit=4&filter=15min&fields=loc,periods.tempC,periods.humidity,periods.windSpeedKPH,periods.weather&client_id=8TgYCRwa05Yfj4leMknpn&client_secret=qKEtajVSpaLbHhgJSdPK7cghRe1Ub3Fk2YU3XR4x")
    data = request.json()
    if not data['success']:
        print("An error occurred: %s" % (data['error']['description']))

    return data

# The code was generated automatically with embedded tool from visualcrossing
# INITIAL CODE AFTER GENERATION WAS NOT WORKING!!!
def get_current_weather_visualcrossing():
    try:

        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/oxford/today?unitGroup=metric&key=VVDTF76WEHNACV5NRL7HBVC44&contentType=json")
        # Parse the results as CSV
        CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        # Parse the results as JSON
        jsonData = json.loads(ResultBytes.code('utf-8'))
    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()

    return jsonData

def get_weather(location, time):
    print("Weather: ")

# Give Post Code, Get Coordinates: https://github.com/ideal-postcodes/postcodes.io
def get_coordinates(post_code = "OX2 9RW"):

    # Check the postcode
    url = "http://api.postcodes.io/postcodes/" + post_code + "/validate"
    response = requests.request("GET", url)
    #print(json.dumps(response.json(), indent=4))

    if not response.json()["result"]:
        raise ValueError("PostCode is wrong!")

    # Get coordinates
    url = "http://api.postcodes.io/postcodes/" + post_code
    response = requests.request("GET", url)
    # print(json.dumps(response.json(), indent=4))

    location = {"lat": response.json()["result"]["latitude"], "lng": response.json()["result"]["longitude"]}
    print("Location: ", location)
    return location

def main():
    post_code = "OX2 9RW"
    location = get_coordinates(post_code)                         # Get Log and Lat
    weather_parameters = get_current_weather(location)            # Get weather by coordinates

    print("Weather data I have for Post Code: " + post_code)
    print(weather_parameters)                                     # Use Weather parameters further...

    print("Another source: ")
    print(get_current_weather_aeris())

    print("Another source #2: ")
    print(get_current_weather_visualcrossing())

if __name__ == '__main__':
    main()
