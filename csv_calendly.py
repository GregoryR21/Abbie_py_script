import requests 
import json
import pandas as pd
import numpy as np
from pprint import pprint

    # 3

    # calls api and stores the data into the variable data
data = requests.get("https://random-data-api.com/api/v2/users?size=50")

    # normalizes the data to make it readable
data2=pd.json_normalize(data.json())


    # converts the normalized dataframe into a csv file
csv_calendly_data = data2.to_csv('csv_calendly_data.csv')