from base import Api, ApiError
from apiKey import api_key

api = Api(api_key)

try:
	product = api.get_product('PPBG')
	print(product)
except ApiError as e:
	print(e.response)
