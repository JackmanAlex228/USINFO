from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("OPENSTATES_API_KEY")
BASE_URL = os.getenv("OPENSTATES_BASE_URL")

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
  
def get_legislator(name):
  """
    Search for bills with a given query
    :param query: The search query
    :return: A JSON object with the bills
  """
  url = f"{BASE_URL}/people"
  params={
    "q": name,
    "apikey": API_KEY
  }
  response = requests.get(url, params=params)
  return response.json() if response.status_code == 200 else response.text