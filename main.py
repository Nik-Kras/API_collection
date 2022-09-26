"""
response.content    # Return the raw bytes of the data payload
response.text       # Return a string representation of the data payload
response.json()     # This method is convenient when the API returns JSON
"""

import requests

def main():
    response = requests.get("https://api.github.com/repos/Nik-Kras/API_collection")
    print(response)
    print("response.content: ", response.content)
    print("response.text: ", response.text)
    print("response.json(): ", response.json())

if __name__ == '__main__':
    main()
