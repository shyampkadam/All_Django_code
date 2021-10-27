#pip install requests

import json
import	requests

URL1="http://127.0.0.1:8000/saveemp/"
emp={
  "id": 2,
  "fullName": "J Vinay",
  "city": "Mumbai",
  "salary": 96000.0
}
jsonData=json.dumps(emp)
responseData=requests.post(url=URL1,data=jsonData)
print(responseData)
