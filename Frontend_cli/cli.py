import sys
import requests
import time

API_BASE = "http://localhost:8000/"
command = sys.argv[1]
if command == 'get':
    key = sys.argv[2]
    url = API_BASE + "get/"
    payload = {'key': key}
    response = requests.request("POST", url, data=payload)
    if response.status_code == 200:
        json = response.json()
        print(json['value'])
    elif response.status_code == 404:
        print("Key Not Found")
    else:
        print("Error")

elif command == 'put':
    key = sys.argv[2]
    value = sys.argv[3]
    url = API_BASE + "update/"
    payload = {'key':key, 'value':value}
    response = requests.request("POST", url, data=payload)
    if response.status_code == 200:
        json = response.json()
        print("Successfully Updated Key")
    else:
        print("Error")

elif command == 'watch':
    url = API_BASE + "time/"
    response = requests.request("GET", url)
    if response.status_code == 200:
        timestamp = response.json()['time']
        url = API_BASE + "watch/"
        while True:
            payload = {'time':timestamp}
            response = requests.request("POST", url, data=payload)
            if response.status_code == 200:
                timestamp = response.json()['last']
                count = response.json()['count']
                for i in range(count):
                    print("Key: " + response.json()['result'][i]['key'] + " Value: " + response.json()['result'][i]['value'])
            time.sleep(0.5)
    else:
        print("Error")
else:
    print("Invalid Syntax")
