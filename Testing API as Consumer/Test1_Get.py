#pip install requests

import	requests

URL1="http://127.0.0.1:8000/showallemp/"
URL2="https://jsonplaceholder.typicode.com/users"
URL3="https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=637ea8e97f5bcbd8ae9675a6bd04dbd5"

URL4="http://127.0.0.1:8000/showemp/2"
apiResponse=requests.get(url=URL4)
jsonResponse=apiResponse.json()
print(jsonResponse)

