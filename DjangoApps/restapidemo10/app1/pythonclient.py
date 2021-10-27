#pip install requests

import	requests

URL1="http://localhost:8000/studentapi/"

apiResponse=requests.get(url=URL1)
jsonResponse=apiResponse.json()
print(jsonResponse)

