import json
import pandas as pd
import numpy as np
import requests
from pprint import pprint
from config import api_key1

def search_restaurants(set_num):

    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer {}'.format(api_key1),
    }
    url_params = { #parameters passed to the API
    "categories": 'restaurants, All',
    "location":"San Francisco",
    "state": "California",
    'offset': offset_num,
     "limit":50
     }

    response = requests.get(url, headers=headers, params=url_params)
    return response.json()


if __name__ == "__main__":
    for offset_num in np.arange(50,1001,50) :
        try:
            output_json = search_restaurants(offset_num)
            print(offset_num)
            print(output_json)
#             with open('yelp_data/rest_'+str(offset_num)+'.json', 'w') as outfile:
#                 json.dump(output_json,outfile)
            if offset_num == 50:
                df_first = pd.DataFrame.from_dict(output_json['businesses'])
            else:
                df2 = pd.DataFrame.from_dict(output_json['businesses'])
                df_first = df_first.append(df2)
        except AttributeError:
            print("error at ", offset_num)
            
    df_first.to_csv("yelp_data/output_rest3test.csv", index = False)
    print(df_first.shape[0])
    print(df_first)