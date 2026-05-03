import requests

r = requests.post("http://localhost:8000/hi", json={"who": "FastAPI"})
print(r.json())
