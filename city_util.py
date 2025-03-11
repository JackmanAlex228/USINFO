from dotenv import load_dotenv
import os
import requests

load_dotenv()

BASE_URL = os.getenv("LEGISTAR_BASE_URL")
endpoint = "Events"

response = requests.get(BASE_URL + endpoint)

if response.status_code == 200:
  data = response.json()
  for event in data[:5]:
    print(f"Evene: {event['EventBodyName']} on {event['EventDate']}")
else:
  print(f"Error: {response.status_code} - {response.text}")