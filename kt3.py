#22.01.2024 Marii

import requests

url = f"https://dummyjson.com/carts"

response = requests.get(url)

# api_key = "sinu_api_voti"


# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    print(data)