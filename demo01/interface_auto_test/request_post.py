import requests
import json

url = "http://localhost:8080/EasyBuy/Login"

data = "loginName=admin&password=123456&action=login"

# response=requests.request("POST",url=url,params=data)
response=requests.post(url,params=data)

# print(response.text)

# print(response.json())

print(json.dumps(response.json(),indent=4,ensure_ascii=False))


