import json
import requests
from pprint import pprint

r = requests.get("https://proagile.se/api/publicEvents")
file = json.loads(r.text)
startList = []
for i in file:
    print(i['startDate'])

