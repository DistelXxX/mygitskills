import jsonpath
import requests
import json

url="http://localhost:8000/login"
data={
    "username": "admin",
    "password": "admin"
}
res=requests.request("POST",url,json=data)
print(json.dumps(res.json(),indent=4,ensure_ascii=False))

print("__________________________________________________")

url01="http://localhost:8000/auth/hello"
token="Bearer " + jsonpath.jsonpath(res.json(),"$..token")[0]
headers={
    "Authorization":token
}
resp=requests.get(url=url01,headers=headers)
print(json.dumps(resp.json(),indent=4,ensure_ascii=False))

print("__________________________________________________")

url02="http://httpbin.org/post"
file=open("c:\\userinfo.txt","rb")
files={
    "file":file
}
respo=requests.post(url=url02,files=files)
print(json.dumps(respo.json(),indent=4,ensure_ascii=False))