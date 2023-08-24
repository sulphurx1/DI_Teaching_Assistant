import requests

response = requests.get('http://localhost:8000/students/')
print(response.json())