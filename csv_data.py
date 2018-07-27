import csv
import json

####################################
####Import Dataset 1 from CSV#######
####################################
with open('Resources/Police_Department_Incidents_-_Previous_Year__2017_.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('Resources/dataset1.json', 'w') as f:
    json.dump(rows, f)
    

####################################
####Import Dataset 2 from CSV#######
####################################
with open('Resources/Police_Department_Incidents_-_Previous_Year__2017_.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('Resources/dataset2.json', 'w') as f:
    json.dump(rows, f)    