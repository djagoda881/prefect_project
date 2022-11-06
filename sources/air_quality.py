import pandas as pd
import requests
import json
from typing import Dict, Any
from datetime import datetime, date, timedelta

url = "https://api.apilayer.com/exchangerates_data/timeseries?"
headers = {"apikey": "wsv9UWyKU8QBv1B8C5U2ej6Q9hnnv05I"}
payload = {
        }
try:
    response = requests.request(
            "GET", url , headers=headers, data={}, params=payload
        )
       
except ConnectionError as e:  
    print(e)
