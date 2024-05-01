

import requests
from config.global_config import *

#api_key = API_KEY

#URL = URL

r = requests.get(url=URL)
result = r.json()
print(result)


