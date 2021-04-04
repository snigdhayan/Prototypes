import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={"worst concave points":0.12,"worst perimeter":100,"mean concave points":0.15})

# Response should be 0 or false

# r = requests.post(url,json={"worst concave points":0.13,"worst perimeter":100,"mean concave points":0.05})

# Response should be 1 or true

print(r.json())