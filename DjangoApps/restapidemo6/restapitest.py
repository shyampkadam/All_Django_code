import requests
import json
URL = "http://127.0.0.1:8000/studentapi/"
def post_data():
    data = {
        'name': 'rohit',
        'roll': 150,
        'city': 'ranchi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
post_data()
