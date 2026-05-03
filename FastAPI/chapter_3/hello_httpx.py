import httpx

r = httpx.get("http://localhost:8000/hi/toksik")
print(r.json())
