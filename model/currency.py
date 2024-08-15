
from sqlalchemy import Column, Integer, VARCHAR, Date, Boolean, Float, TIMESTAMP
import sys
sys.path.append("..")



from model.base import Base

class Weather(Base):
    __tablename__ = 'df_weather'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    cities = Column(VARCHAR(100), nullable=False)
    temperature = Column(Float, nullable=False)
    cloudiness = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False, index=True)