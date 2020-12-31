# FLASK / REACT App for Home Values
# originally setup with this: https://www.youtube.com/watch?v=Q2eafQYgglM
#    -> corresponding blog post -> https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project

### REQS

import time
from flask import Flask
app = Flask(__name__)

import pandas as pd





@app.route('/time')
def get_current_time():
	return {'time': time.time()}


### Zip Code Data API

# get all zips
all_zips = pd.read_csv('data/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon.csv', nrows=10)

# returning all values
@app.route('/values')
def get_all_values():
	return {'values': all_zips.to_json()}