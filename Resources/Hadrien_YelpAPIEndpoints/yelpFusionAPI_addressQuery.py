# https://www.yelp.com/developers/documentation/v3/business_search
import json
import pandas as pd
import numpy as np
import requests
from pprint import pprint
import time
from config import api_key1

if __name__ == "__main__":
    
    
    
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer {}'.format(api_key1),
    }
    address = ["576 haight st",
             "1801 haight st",
              "865 market st",
         "2155 bayshore blvd",
             "752 jackson st",
          "5 embarcadero ctr",
               "523 broadway",
           "347 presidio ave",
               "1360 9th ave",
          "762 divisadero st",
        "280 golden gate ave",
              "314 sutter st",
              "314 sutter st",
             "1307 sutter st",
                "200 pine st",
             "575 mission st",
             "622 jackson st",
             "1351 church st",
           "2049 fillmore st",
               "121 spear st",
         "1494 california st",
               "73 cambon dr",
            "6 monterey blvd",
              "937 howard st",
           "925 cortland ave",
               "1865 post st",
           "500 presidio ave",
               "3275 22nd st",
               "3275 22nd st",
            "3438 mission st",
            "59 columbus ave",
            "3226 mission st",
             "2605 ocean ave",
             "2605 ocean ave",
            "3230 mission st",
                "713 clay st",
         "2827 california st",
               "1453 18th st",
             "836 clement st"]
    
    url_params = { #parameters passed to the API
    "categories": 'restaurants, All',
    "location":"San Francisco",
    "state": "California",
    "address1":address,
    "is_closed": True,
    'offset': 50,
     "limit":50
     }
    
    all_responses = []

    for addresses in address:
        responses = all_responses.append(requests.get(url, headers=headers, params=url_params).json())
        print(all_responses)