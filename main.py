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

def main():

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

if __name__ == '__main__':
    main()
