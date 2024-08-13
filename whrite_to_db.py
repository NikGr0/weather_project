
import time
import requests
import yaml
from config.global_config import *
import datetime as datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append("..")

from model.base import Base
from model.currency import Currency


# читаем список городов
with open(r'config\list_cities.yaml') as file:
    list_cities = yaml.load(file, Loader=yaml.FullLoader)


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

