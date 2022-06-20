import requests

urlBase="http://127.0.0.1:5000/"
headers = {"Content-Type": "application/json"}

response=requests.put(urlBase+"operation/1", {"Numero":5}, headers=headers)

print(response.json())