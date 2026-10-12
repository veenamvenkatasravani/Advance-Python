import requests

print("Requests version:", requests.__version__)

response = requests.get(
    "https://example.com",
    timeout=10
)

print("Status code:", response.status_code)
print("Website response:", response.text[:100])