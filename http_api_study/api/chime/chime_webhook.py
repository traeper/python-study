import json
import requests

API_URL = 'https://hooks.chime.aws/incomingwebhooks/ce5475e9-cb90-419f-8c89-81c0047684dd?token=bDhKaHd3OXV8MXxtV1YwWGFGVXRFQUN3b2lHSGNrdVV1OVFIN0lzckRRWmp3WVloVGtVTEY4'
headers = {'Content-Type': 'application/json'}

json_data = {'Content': 'https://google.com'}

response = requests.post(API_URL, headers=headers, json=json_data)

if response.status_code == 200:
    print("API Communication Successfully Completed!!")
    print(json.loads(response.content.decode('utf-8')))
else:
    print("API Call Failed.. TT")
