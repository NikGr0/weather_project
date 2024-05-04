import time

import requests
import yaml
import datetime
import pandas as pd
from config.global_config import *
import config as con

# with open(r'config\list_cities.yaml', 'w') as file:
#     doc = yaml.dump(['51.7727,55.0988', '', '59.9386,30.3141', '56.8519,60.6122', '55.0415,82.9346'], file)

# читаем список городов
with open(r'config\list_cities.yaml') as file:
    list_cities = yaml.load(file, Loader=yaml.FullLoader)
print(list_cities)

# получаем название файла csv
dt1 = datetime.datetime.now()
dt_now = 'history/' + str(dt1)[:-7]
print(dt_now)
# получаем данные
weather = []
for i in list_cities:
    r = requests.get(url=URL + f'{API_KEY}&q={i}')
    result = r.json()

    city = result.get('location').get('name')
    temp = result.get('current').get('temp_c')
    cloud = result.get('current').get('cloud')

    d = {'Город': city,
         'Температура, °С': temp,
         'Облачность, %': cloud
         }
    weather.append(d)
    time.sleep(1)
#print(d)
print(weather)

from_history = pd.DataFrame(weather)
from_history.to_csv(dt_now)
