# This turned to be a failed experiment to return all results beyond the 1,000 results allowed by the Yelp Fusion Business Search API.
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
    zipcode = [94151, 94159, 94158, 94102, 94104, 94103, 94105, 94108, 94177, 94107, 94110, 94109, 94112, 94111, 94115, 
               94114, 94117, 94116, 94118, 94121, 94123, 94122, 94124, 94127, 94126, 94129, 94131, 94133, 94132, 94134, 94139, 94143]
    url_params = { #parameters passed to the API
    "categories": 'restaurants, All',
    "location":"San Francisco",
    "state": "California",
    "zip_code":zipcode,
    'offset': 50,
     "limit":50
     }
    
    all_responses = []

    for i, zipcodes in enumerate(zipcode):
        time.sleep(30)
     
        for offset_num in np.arange(50,1000,50) :

            try:
                url_params["offset"]=offset_num
                all_responses.append(requests.get(url, headers=headers, params=url_params).json())
                print(all_responses)

                if offset_num == 50:
                    df_first = pd.DataFrame.from_dict(all_responses[i]['businesses'])
                else:
                    df2 = pd.DataFrame.from_dict(all_responses[i]['businesses'])
                    df_first = df_first.append(df2)
            except AttributeError:
                print("error at ", offset_num)
            
            df_first.to_csv(f"yelp_data/yelpData_byZips/output_zipsearch_{zipcodes}.csv", index = False)