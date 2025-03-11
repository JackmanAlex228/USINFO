from state_federal_util import *
from dotenv import load_dotenv
import os

print(f"\nget_bills:\n{get_bills()}")
print(f"\nget_legislator:\n{get_legislator("Stephanie Gricius")}")

## TODO: Plan out the informational structure of the application and what APIs to use
## TODO: Look for free APIs that refer to city-level information