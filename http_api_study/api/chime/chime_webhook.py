import json
import requests

API_URL = 'https://hooks.chime.aws/incomingwebhooks/34bc8326-da51-49b7-85ae-a7a459f24701?token=Y3huOWdlenF8MXx3QVh2NmFoRkI4T0ZpR1BfYTB1bHZ3dlkzSzNPQk5wSUtEa3N3SHlQTzZF'
headers = {'Content-Type': 'application/json'}

json_data = {'Content': 'hello, jiyoung.'}

response = requests.post(API_URL, headers=headers, json=json_data)

if response.status_code == 200:
    print("API Communication Successfully Completed!!")
    print(json.loads(response.content.decode('utf-8')))
else:
    print("API Call Failed.. TT")

# HTML Response Code
# 200 Successfuly Completed.
# 3XX
# 404 page not found.
# 500 Internal Server Error
# 503 Gateway..