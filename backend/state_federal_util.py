from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
API_KEY = os.getenv("OPENSTATES_API_KEY")
BASE_URL = os.getenv("OPENSTATES_BASE_URL")

# Data to fetch for state and federal legislators
# - Name
# - Party
# - District
# - Chamber
# - State
# - Campaign donations
# - Bills sponsored
# - Bills co-sponsored
# - Committees
# - Votes
# - Contact information
# - Social media accounts

# Data to fetch for state and federal departments
# - Name
# - Department
# - Budget
# - Services
# - Contact information
# - Social media accounts
# - Location
# - Services provided
# - Programs

def get_bills(state ="ut", session="2024"):
  """
    Get all the bills for a given state and session
    :param state: The state abbreviation
    :param session: The session year
    :return: A JSON object with the bills
  """
  url = f"{BASE_URL}/bills"
  params={
    "jurisdiction": state,
    "session": session,
    "apikey": API_KEY
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:
    return response.json()
  else:
    return {"error": response.status_code, "message": response.text}

def get_legislators(jurisdiction):
  """
    Search for bills with a given query
    :param query: The search query
    :return: A JSON object with the legislators
  """
  url = f"{BASE_URL}/people"
  params={
    "jurisdiction": jurisdiction,
    "apikey": API_KEY
  }
  response = requests.get(url, params=params)
  return response.json() if response.status_code == 200 else response.text

output = json.dumps(get_legislators("Utah"), indent=4)
legislators = json.loads(output)
for legislator in legislators.get("results", []):
  name = legislator.get("name", "N/A")
  party = legislator.get("party", "N/A")
  print(f"Name: {name}, Party: {party}")