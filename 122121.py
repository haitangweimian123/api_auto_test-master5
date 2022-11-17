import json

import requests

url="http://10.0.88.13/jeecgboot/base/quoted/accountFixedRate/add"
headers={"X-Access-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjYwNTk1NDEsInVzZXJuYW1lIjoiYWRtaW4ifQ.EeujIJahqWnhus37CW1xmLJGxS5MYPESZ7nZGn7v-GU",
         "Content-Type": "application/json;charset=UTF-8"}

data={
  "orderType": "02",
  "orderTypeName": "样品线",
  "eqtName": "1",
  "accCategory": "1",
  "accDetails": "1",
  "fixedRate": 1
}
reqs=requests.post(url,headers=headers,data=json.dumps(data))

print(reqs.text)