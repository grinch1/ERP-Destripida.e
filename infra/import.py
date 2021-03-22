from api import Api, ApiError
from apiKey import api_key
from connection import Database
import pandas as pd

api = Api(api_key)

db = Database()
db.close()

try:
	product = api.get_products()
	df = pd.DataFrame(product)
	print(df)
except ApiError as e:
	print(e.response)