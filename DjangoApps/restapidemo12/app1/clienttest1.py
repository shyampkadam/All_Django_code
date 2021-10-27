import requests
url = 'http://localhost:8000/studentapi/'
headers = {
'Authorization': 'Token 09ec8a0850e6862dfa7145cf7088b196d5dec411'
}
r = requests.get(url, headers=headers)
print(r.json())