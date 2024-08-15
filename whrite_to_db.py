# Запись в погоды в базу данных
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
from model.currency import Weather


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_local = SessionLocal()

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

    new_record = Weather(
                cities=city,
                temperature=temp,
                cloudiness=cloud,
                create_time=datetime.datetime.now()
                )

    session_local.add(new_record)
    time.sleep(1)

session_local.commit()